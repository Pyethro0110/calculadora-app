import streamlit as st
import math
import re

st.set_page_config(page_title="Calc Pro", layout="centered")

# =========================
# ESTADO
# =========================
if "expr" not in st.session_state:
    st.session_state.expr = ""

if "page" not in st.session_state:
    st.session_state.page = "calc"

if "mem" not in st.session_state:
    st.session_state.mem = 0

if "history" not in st.session_state:
    st.session_state.history = []

# =========================
# CSS FORTE (FUNCIONA NO MOBILE)
# =========================
st.markdown("""
<style>

.stApp {
    background: #0a0f1c;
    color: white;
}

/* LARGURA FIXA IGUAL EM QUALQUER TELA */
.block-container {
    max-width: 420px;
    margin: auto;
}

/* DISPLAY */
.display {
    background: #111827;
    padding: 25px;
    border-radius: 18px;
    font-size: 32px;
    text-align: right;
    margin-bottom: 10px;
}

/* BOTÕES GRANDES REAIS */
button {
    height: 70px !important;
    font-size: 22px !important;
    border-radius: 14px !important;
    font-weight: bold !important;
}

/* CORES GARANTIDAS (IMPORTANTE) */
div[data-testid="stButton"] button {
    background: #1f2937;
    color: white;
}

/* OPERADORES */
.op button {
    background: #f97316 !important;
}

/* IGUAL */
.eq button {
    background: #22c55e !important;
}

/* MENU */
.topbar {
    display: flex;
    justify-content: space-between;
    margin-bottom: 10px;
}

.menu-btn button {
    background: #3b82f6 !important;
}

</style>
""", unsafe_allow_html=True)

# =========================
# FUNÇÕES
# =========================
def add(v):
    st.session_state.expr += str(v)

def clear():
    st.session_state.expr = ""

def back():
    st.session_state.expr = st.session_state.expr[:-1]

def safe_eval(expr):
    expr = expr.replace("×", "*").replace("÷", "/")
    if not re.match(r"^[0-9+\-*/(). ]*$", expr):
        return "Erro"
    try:
        return eval(expr, {"__builtins__": None}, {})
    except:
        return "Erro"

# =========================
# MENU TOPO (SEM TRAVAR TELA)
# =========================
col1, col2, col3 = st.columns([1, 4, 1])

with col1:
    if st.button("≡"):
        st.session_state.page = "menu"

with col3:
    if st.button("⌂"):
        st.session_state.page = "calc"

# =========================
# TELA PRINCIPAL
# =========================
st.title("Calculadora Pro")

# =========================
# PÁGINA MENU (NÃO TRAVA)
# =========================
if st.session_state.page == "menu":

    if st.button("Logaritmo"):
        st.session_state.page = "log"

    if st.button("Temperatura"):
        st.session_state.page = "temp"

    if st.button("Medidas"):
        st.session_state.page = "med"

    if st.button("Memória"):
        st.session_state.page = "mem"

# =========================
# CALCULADORA
# =========================
elif st.session_state.page == "calc":

    st.markdown(f"""
    <div class="display">
    {st.session_state.expr or "0"}
    </div>
    """, unsafe_allow_html=True)

    col = st.columns(4)

    col[0].button("C", on_click=clear)
    col[1].button("⌫", on_click=back)
    col[2].button("%", on_click=lambda: add("%"))
    col[3].button("÷", on_click=lambda: add("÷"))

    col = st.columns(4)
    col[0].button("7", on_click=lambda: add("7"))
    col[1].button("8", on_click=lambda: add("8"))
    col[2].button("9", on_click=lambda: add("9"))
    col[3].button("×", on_click=lambda: add("×"))

    col = st.columns(4)
    col[0].button("4", on_click=lambda: add("4"))
    col[1].button("5", on_click=lambda: add("5"))
    col[2].button("6", on_click=lambda: add("6"))
    col[3].button("-", on_click=lambda: add("-"))

    col = st.columns(4)
    col[0].button("1", on_click=lambda: add("1"))
    col[1].button("2", on_click=lambda: add("2"))
    col[2].button("3", on_click=lambda: add("3"))
    col[3].button("+", on_click=lambda: add("+"))

    col = st.columns(4)
    col[0].button("0", on_click=lambda: add("0"))
    col[1].button(".", on_click=lambda: add("."))

    col[2].button("M+", on_click=lambda: st.session_state.update(mem=st.session_state.mem + (safe_eval(st.session_state.expr) if st.session_state.expr else 0)))

    col[3].button("=", on_click=lambda: (
        st.session_state.history.append(f"{st.session_state.expr}={safe_eval(st.session_state.expr)}"),
        st.session_state.__setattr__("expr", str(safe_eval(st.session_state.expr)))
    ))

# =========================
# LOG (SAI DA TELA SOZINHO)
# =========================
elif st.session_state.page == "log":

    n = st.number_input("Log base 10", value=1.0)

    if st.button("Calcular"):
        st.success(math.log10(n))
        st.session_state.page = "calc"   # VOLTA AUTOMATICAMENTE

# =========================
# TEMPERATURA
# =========================
elif st.session_state.page == "temp":

    t = st.number_input("Temperatura", value=0.0)
    tipo = st.selectbox("Tipo", ["C→F", "F→C", "C→K"])

    if st.button("Converter"):
        if tipo == "C→F":
            r = (t*9/5)+32
        elif tipo == "F→C":
            r = (t-32)*5/9
        else:
            r = t+273.15

        st.success(r)
        st.session_state.page = "calc"  # VOLTA SOZINHO

# =========================
# MEDIDAS
# =========================
elif st.session_state.page == "med":

    m = st.number_input("Metros", value=1.0)

    if st.button("Converter"):
        st.success(f"{m} m = {m*100} cm")
        st.session_state.page = "calc"

# =========================
# MEMÓRIA
# =========================
elif st.session_state.page == "mem":

    st.write("Memória:", st.session_state.mem)

    if st.button("MC"):
        st.session_state.mem = 0

    if st.button("MR"):
        st.session_state.expr += str(st.session_state.mem)

    if st.button("Voltar"):
        st.session_state.page = "calc"

# =========================
# HISTÓRICO
# =========================
st.markdown("---")
st.subheader("Histórico")

if st.button("Limpar"):
    st.session_state.history = []

for item in st.session_state.history[-10:]:
    st.write(item)
