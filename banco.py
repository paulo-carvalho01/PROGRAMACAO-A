from decimal import Decimal, InvalidOperation
from itertools import count

from flask import Flask, flash, redirect, render_template, request, url_for

app = Flask(__name__)
app.secret_key = "banco-dcomp-prototipo"

clientes = {}
contas = {}
proximo_numero_conta = count(1001)


def converter_valor(valor):
    try:
        quantia = Decimal(valor.replace(",", "."))
    except (InvalidOperation, AttributeError):
        return None

    if not quantia.is_finite():
        return None

    return quantia.quantize(Decimal("0.01"))


@app.get("/")
def inicio():
    numero = request.args.get("numero", "").strip()
    conta_consultada = contas.get(numero) if numero else None

    if numero and conta_consultada is None:
        flash("Conta não encontrada.", "erro")

    return render_template(
        "index.html",
        clientes=clientes.values(),
        contas=contas.values(),
        conta_consultada=conta_consultada,
        numero_consultado=numero,
    )


@app.post("/clientes")
def cadastrar_cliente():
    nome = request.form.get("nome", "").strip()
    cpf = request.form.get("cpf", "").strip()
    idade_texto = request.form.get("idade", "").strip()

    if not nome or not cpf.isdigit() or len(cpf) != 11:
        flash("Informe um nome e um CPF com exatamente 11 dígitos.", "erro")
        return redirect(url_for("inicio"))

    try:
        idade = int(idade_texto)
    except ValueError:
        flash("Informe uma idade válida.", "erro")
        return redirect(url_for("inicio"))

    if idade < 0:
        flash("A idade não pode ser negativa.", "erro")
        return redirect(url_for("inicio"))

    if cpf in clientes:
        flash("Já existe um cliente cadastrado com esse CPF.", "erro")
        return redirect(url_for("inicio"))

    clientes[cpf] = {"nome": nome, "cpf": cpf, "idade": idade}
    flash(f"Cliente {nome} cadastrado com sucesso.", "sucesso")
    return redirect(url_for("inicio"))


@app.post("/contas")
def criar_conta():
    cpf = request.form.get("cpf", "").strip()
    cliente = clientes.get(cpf)

    if cliente is None:
        flash("Cliente não encontrado. Cadastre o cliente antes de criar a conta.", "erro")
        return redirect(url_for("inicio"))

    saldo = converter_valor(request.form.get("saldo_inicial", "0"))
    if saldo is None or saldo < 0:
        flash("Informe um saldo inicial válido e não negativo.", "erro")
        return redirect(url_for("inicio"))

    numero = str(next(proximo_numero_conta))
    contas[numero] = {
        **cliente,
        "numero": numero,
        "saldo": saldo,
    }
    flash(f"Conta {numero} criada para {cliente['nome']}.", "sucesso")
    return redirect(url_for("inicio"))


@app.post("/contas/buscar")
def buscar_conta():
    numero = request.form.get("numero", "").strip()
    return redirect(url_for("inicio", numero=numero))


@app.post("/contas/<numero>/<operacao>")
def movimentar_conta(numero, operacao):
    conta = contas.get(numero)
    if conta is None:
        flash("Conta não encontrada.", "erro")
        return redirect(url_for("inicio"))

    if operacao not in {"depositar", "sacar"}:
        return "Operação inválida.", 404

    valor = converter_valor(request.form.get("valor", ""))
    if valor is None or valor <= 0:
        flash("Informe um valor válido e maior que zero.", "erro")
        return redirect(url_for("inicio", numero=numero))

    if operacao == "sacar" and valor > conta["saldo"]:
        flash("Saldo insuficiente para realizar o saque.", "erro")
        return redirect(url_for("inicio", numero=numero))

    if operacao == "depositar":
        conta["saldo"] += valor
        flash(f"Depósito de R$ {valor:.2f} realizado com sucesso.", "sucesso")
    else:
        conta["saldo"] -= valor
        flash(f"Saque de R$ {valor:.2f} realizado com sucesso.", "sucesso")

    return redirect(url_for("inicio", numero=numero))


if __name__ == "__main__":
    app.run()
