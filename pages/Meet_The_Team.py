import streamlit as st

st.title("Meet The Team")

st.markdown(
    """We are a group of students who are passionate about data science."""
)

row_1 = st.container()

row_1_col_1, row_1_col_2, row_1_col_3, row_1_col_4 = row_1.columns(4)

with row_1_col_1:
    st.image("images/the_team/lucy_ahern.jpg")
    st.write("Lucy Ahern")

with row_1_col_2:
    st.image("images/the_team/gavin_kelly.jpg")
    st.write("Gavin Kelly")

with row_1_col_3:
    st.image("images/the_team/georgia_whitton.jpg")
    st.write("Georgia Whitton")

with row_1_col_4:
    st.image("images/the_team/hui_gong.jpg")
    st.write("Hui Gong")

row_2 = st.container()

row_2_col_1, row_2_col_2, row_2_col_3, row_2_col_4 = row_2.columns(4)

with row_2_col_1:
    st.image("images/the_team/marta_sadlej.jpg")
    st.write("Marta Sadlej")

with row_2_col_2:
    st.image("images/the_team/reem_abouward.jpg")
    st.write("Reem Abouward")

with row_2_col_3:
    st.image("images/the_team/sara_patti.jpg")
    st.write("Sara Patti")

with row_2_col_4:
    st.image("images/the_team/tamara_hodgetts.jpg")
    st.write("Tamara Hodgetts")

row_3 = st.container()

row_3_col_1, row_3_col_2, row_3_col_3, row_3_col_4 = row_3.columns(4)

with row_2_col_1:
    st.image("images/the_team/yewmun_yip.jpg")
    st.write("Yew Mun Yip")

with row_2_col_2:
    st.image("images/the_team/spencer_duvwiama.jpg")
    st.write("Sepencer Duvwiama")

with row_2_col_3:
    st.image("images/the_team/eschal_najmi.jpg")
    st.write("Eschal Najmi")

with row_2_col_4:
    st.image("images/the_team/xianglu_xiao.jpg")
    st.write("Xianglu Xiao")

# row_4 = st.container()

# row_4_col_1, row_4_col_2, row_4_col_3, row_4_col_4 = row_4.columns(4)
