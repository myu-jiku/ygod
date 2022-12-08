"""
YGO Destiny – A Yu-Gi-Oh! sealed draft simulator written in rust.
Copyright (C) 2022  myujiku

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License version 3 as
published by the Free Software Foundation.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

import project, xml
from gtk_xml import (
    GtkChildObject,
    GtkMargins,
    GtkObject,
    GtkProperty,
    GtkTrue,
    GtkFalse,
)
from xml import XmlTag

class_name = "YGONewCollectionWindow"
parent_class = "AdwWindow"


content = (
    GtkProperty("title", "New Collection"),
    GtkProperty("modal", GtkTrue),
    GtkProperty("default-width", "600"),
    GtkProperty("default-height", "400"),
    GtkProperty("resizable", GtkFalse),
    GtkProperty("content", GtkObject(
        "GtkBox",
        (
            GtkProperty("orientation", "vertical"),
            GtkChildObject("GtkHeaderBar"),
        )
    )),
)


gtk_template = XmlTag(
    "template",
    options={
        "class": class_name,
        "parent": parent_class,
    },
    content=content,
)

xml_content = XmlTag("interface", gtk_template)

xml.save_to_file(
    f"{project.directory}/{__name__.split('.')[-1]}.ui", xml_content, project.header
)