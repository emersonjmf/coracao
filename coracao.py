import streamlit as st

st.set_page_config(page_title="❤️ Meu Coração para Você ❤️", layout="centered")

# Título principal
st.title("❤️ Para o Amor da Minha Vida ❤️")

# Coração gigante feito com emoji
st.markdown(
    """
    <div style="font-size:150px; text-align:center; line-height:1;">
        ❤️
    </div>
    """,
    unsafe_allow_html=True
)

# Mensagem carinhosa
st.write("""
Desde que você entrou na minha vida,  
meu coração só sabe bater por você.  

Te amo demais! 💖  
""")

# Um botão para mostrar uma surpresa
if st.button('Clique aqui para uma surpresa'):
    st.balloons()
    st.success("Você é incrível! Te amo demais! 💘")