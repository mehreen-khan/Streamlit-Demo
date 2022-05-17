import streamlit as st
from streamlit_option_menu import option_menu
from apps import home, heatmap, upload  # import your app modules here

st.set_page_config(page_title="Streamlit Geospatial", layout="wide")

# A dictionary of apps in the format of {"App title": "App icon"}
# More icons can be found here: https://icons.getbootstrap.com

apps = [
    {"func": home.app, "title": "Home Page 1", "icon": "house"},
    {"func": heatmap.app, "title": "Heatmap Page 2", "icon": "map"},
    {"func": upload.app, "title": "Upload Page 3", "icon": "cloud-upload"},
]

titles = [app["title"] for app in apps]
titles_lower = [title.lower() for title in titles]
icons = [app["icon"] for app in apps]

params = st.experimental_get_query_params()

if "page" in params:
    default_index = int(titles_lower.index(params["page"][0].lower()))
else:
    default_index = 0

with st.sidebar:
    selected = option_menu(
        "Main Menu",
        options=titles,
        icons=icons,
        menu_icon="cast",
        default_index=default_index,
    )

    st.sidebar.title("About")
    st.sidebar.info(
        """
        This web [app](https://github.com/mehreen-khan) is maintained by [](https://www.iari.res.in/). This is the demo for the framework of Geospatial InfoCrop:
            [GitHub](https://github.com/mehreen-khan)| [LinkedIn](https://www.linkedin.com/in/qiushengwu).
        
        Source code: <https://github.com/giswqs/streamlit-template>

        More menu icons: <https://icons.getbootstrap.com>
    """
    )

for app in apps:
    if app["title"] == selected:
        app["func"]()
        break
