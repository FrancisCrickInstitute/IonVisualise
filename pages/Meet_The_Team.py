import streamlit as st

st.title("Meet The Team")

st.markdown(
    """We are a group of scientists who are passionate about data science."""
)

row_1 = st.container()

row_1_col_1, row_1_col_2, row_1_col_3, row_1_col_4 = row_1.columns(4)

with row_1_col_1:
    st.image("images/the_team/lucy_ahern.jpg")
    st.write("Lucy Ahern")
    st.markdown(
        '<a href="mailto:lucy.ahern@crick.ac.uk">lucy.ahern@crick.ac.uk</a>',
        unsafe_allow_html=True,
    )

with row_1_col_2:
    st.image("images/the_team/gavin_kelly.jpg")
    st.write("Gavin Kelly")
    st.markdown(
        '<a href="mailto:Gavin.Kelly@crick.ac.uk">Gavin.Kelly@crick.ac.uk</a>',
        unsafe_allow_html=True,
    )

with row_1_col_3:
    st.image("images/the_team/georgia_whitton.jpg")
    st.write("Georgia Whitton")
    st.markdown(
        '<a href="mailto:georgia.whitton@crick.ac.uk">georgia.whitton@crick.ac.uk</a>',
        unsafe_allow_html=True,
    )

with row_1_col_4:
    st.image("images/the_team/hui_gong.jpg")
    st.write("Hui Gong")
    st.markdown(
        '<a href="mailto:hui.gong@crick.ac.uk">hui.gong@crick.ac.uk</a>',
        unsafe_allow_html=True,
    )

row_2 = st.container()

row_2_col_1, row_2_col_2, row_2_col_3, row_2_col_4 = row_2.columns(4)

with row_2_col_1:
    st.image("images/the_team/marta_sadlej.jpg")
    st.write("Marta Sadlej")
    st.markdown(
        '<a href="mailto:marta.sadlej@crick.ac.uk">marta.sadlej@crick.ac.uk</a>',
        unsafe_allow_html=True,
    )

with row_2_col_2:
    st.image("images/the_team/reem_abouward.jpg")
    st.write("Reem Abouward")
    st.markdown(
        '<a href="mailto:reem.abouward@crick.ac.uk">reem.abouward@crick.ac.uk</a>',
        unsafe_allow_html=True,
    )

with row_2_col_3:
    st.image("images/the_team/sara_patti.jpg")
    st.write("Sara Patti")
    st.markdown(
        '<a href="mailto:sara.patti@crick.ac.uk">sara.patti@crick.ac.uk</a>',
        unsafe_allow_html=True,
    )

with row_2_col_4:
    st.image("images/the_team/tamara_hodgetts.jpg")
    st.write("Tamara Hodgetts")
    st.markdown(
        '<a href="mailto:tamara.hodgetts@crick.ac.uk">tamara.hodgetts@crick.ac.uk</a>',
        unsafe_allow_html=True,
    )

row_3 = st.container()

row_3_col_1, row_3_col_2, row_3_col_3, row_3_col_4 = row_3.columns(4)

with row_2_col_1:
    st.image("images/the_team/yewmun_yip.jpg")
    st.write("Yew Mun Yip")
    st.markdown(
        '<a href="mailto:yewmun.yip@crick.ac.uk">yewmun.yip@crick.ac.uk</a>',
        unsafe_allow_html=True,
    )

with row_2_col_2:
    st.image("images/the_team/spencer_duvwiama.jpg")
    st.write("Spencer Duvwiama")
    st.markdown(
        '<a href="https://www.linkedin.com/in/spencerduvwiama/">LinkedIn</a>',
        unsafe_allow_html=True,
    )

with row_2_col_3:
    st.image("images/the_team/eschal_najmi.jpg")
    st.write("Eschal Najmi")
    st.markdown(
        '<a href="mailto:eschal.najmi@crick.ac.uk">eschal.najmi@crick.ac.uk</a>',
        unsafe_allow_html=True,
    )

with row_2_col_4:
    st.image("images/the_team/xianglu_xiao.jpg")
    st.write("Xianglu Xiao")
    st.markdown(
        '<a href="mailto:XiangLu.xiao17@imperial.ac.uk">XiangLu.xiao17@imperial.ac.uk</a>',
        unsafe_allow_html=True,
    )
    st.markdown(
        '<a href="https://www.linkedin.com/in/xianglu-xiao/">LinkedIn</a>',
        unsafe_allow_html=True,
    )

# row_4 = st.container()

# row_4_col_1, row_4_col_2, row_4_col_3, row_4_col_4 = row_4.columns(4)
