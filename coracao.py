import streamlit as st

st.set_page_config(page_title="❤️ Pra Você, Meu Amor ❤️", layout="centered")

# Título
st.title("🌹 Para a mulher que ilumina meus dias 🌹")

# Coração gigante com estilo
st.markdown(
    """
    <div style="font-size:140px; text-align:center; line-height:1;">
        💖
    </div>
    """,
    unsafe_allow_html=True
)

# Mensagem carinhosa
st.write("""
Amor da minha vida,  

Desde que te conheci, tudo ganhou mais cor,  
o tempo passou a ter mais sentido,  
e meu coração encontrou o seu lugar.  

Você é o meu porto seguro,  
minha paz em dias difíceis,  
minha risada favorita,  
meu amor eterno. 💘

Obrigado por existir. 🌟  
""")

# Botão com surpresa
if st.button("Clique aqui se você também me ama ❤️"):
    st.balloons()
    st.success("Sabia que você ia clicar! Eu te amo infinitamente 💌")
    