D-CAD-L 2D Tutorial
-------------------

The purpose of this tutorial is to provide a description of the
Dietrich’s D-CAD-L 2D drawing software, which is a part of the
Dietrich’s construction software system.

This tutorial focuses on how to use the D-CAD-L 2D drawing software and
how to set up customized drawing properties, such as page layouts and
dimension style. Methods to draw, edit and dimension drawings will be
explained with the help of a step-by-step sample drawing done with
D-CAD-L 2D. Additional functions, such as layers and libraries, will be
explained as well.


Dietrich’s provides a freeware of the drawing program D-CAD 2D. This
fully functional 2D CAD Program is called D-CAD-L. D-CAD-L can be used
to read and change D- CAD 2D drawings. Therefore, this tutorial can also
be applied for the use of D-CAD 2D.

The only limitation of D-CAD-L is that it is not possible to insert
drawings stored in the Dietrich’s construction software.

Please visit the Dietrich’s homepage to download the software and for
further information
(\ `www.dietrichs.com/en <https://www.google.com/url?q=http://www.dietrichs.com/en)&sa=D&source=editors&ust=1711141313829139&usg=AOvVaw0J6P5Urx5zq0zOBol1qMeH>`__\ `). <https://www.google.com/url?q=http://www.dietrichs.com/en)&sa=D&source=editors&ust=1711141313829398&usg=AOvVaw0pLMdrZiRC4yC5Bp3Rbnly>`__

First steps
-----------

First, an overview of the general D-CAD-L 2D operating mode shall be
provided.

To be able to draw with the plan software, at least one view port is
necessary. View ports can be created by starting a new drawing. However,
it is always possible to change view ports and to add or delete them.

Furthermore, every view port has its own scale. When starting a new view
port, it always asks for the scale. If the scale of a view port is
changed, all objects in it will be changed.

However, the font size is always shown in the absolute size. That means,
if a font size of 3mm is chosen, the heights of the letters will always
be 3mm, independent of the drawing scale. The Font size is settable; on
paper or absolute.

In addition, it is possible to draw beside view ports on an unlimited
drawing area. For that purpose, the zoom function has to be activated (7
View ports 🡪 8 Full screen). A green box shows the position of the view
port. Therefore, the view port shows a section (cut out) of the drawing
area.

The following chapters explain how to start the D-CAD 2D drawing
software and how to organize, draw and edit drawings.

How to start D-CAD-L 2D
^^^^^^^^^^^^^^^^^^^^^^^

Start D-CAD-L 2D by using the icon:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The icon  to start D-CAD-L 2D can be found on your desktop after
installing the program.

Open Drawing
^^^^^^^^^^^^

Here you can open an existing or start a new one.

New Drawing
^^^^^^^^^^^

After having started D-CAD-L 2D, a window pops up to ask for the paper
size and the orientation of a new drawing. Select either a drawing
template or individual settings.

Drawing template: A drawing template with all the settings completed can
be selected. Using a template, the other settings will be greyed out.

The following chapters will explain how to save customized drawing
templates.

Drawing info: Here you can type in for example (garage) for you
information.

Printing device: It is possible to select an output device (printer) for
the drawing. The list contains all printers available on your system.
The selected printer will have an effect on the list of paper sizes.

“User defined formats” can be selected if there is no printer installed
or the drawing should not be specified yet. How to create user defined
formats will be explained later.

Paper size: The available paper sizes and the border settings for each
page are taken from the printer device previously selected.

Orientation: The paper orientation can be chosen, such as landscape and
portrait.

Drawing Header: For the header, select either your address, including
the project information, or only your address. (In PlanCad-L you can
only chose Address.)

Create frame: It is possible to create a frame automatically around the
drawing in thick or thin lines.

View ports: View ports are spaces on paper that contain drawing objects.
Each view port has its own properties, such as scale, coordinate system
and layers.

One, two or four view ports can be arranged automatically on the
drawing. It is possible to add and remove view ports later on.

D-CAD 2D screen

Settings
^^^^^^^^

The following chapters explain how to customize drawings. Procedures for
setting up general settings, such as screen settings and paper sizes, as
well as style settings, such as drawing, dimension and text styles will
be shown.

In the end, it will be explained how to save the drawing with the
completed settings as a drawing template.

General settings
^^^^^^^^^^^^^^^^

This chapter explains how to set up display settings, color set,
toolbars, units, object snap and page layouts as well as message time,
auto save and do/undo steps.

Color set:
^^^^^^^^^^



Screen settings window
----------------------

This window defines the colors used in D-CAD-L 2D. Color sets always
consist of two colors. One for white background color and one for black
background color. The background color can be changed in the General
settings.

New color sets can be added by entering a name and selecting the color.

Color set window
^^^^^^^^^^^^^^^^

Toolbar
^^^^^^^

Individual toolbars can be selected in the toolbar window. It is
possible to create new toolbars, to edit existing ones and to delete
them.

Toolbar window        New toolbar window

The “default” button will reset the toolbars to the default settings.

Units
^^^^^

It is possible to change the unit system of D-CAD-L 2D. In this
tutorial, the unit “meter” will be used.

Unit’s window

A shortcut for the current unit, e.g. “ft” for “feet-inch”, is shown in
the status bar in the right lower corner of the screen. The status bar
can be shown and hidden in the General settings window.

Object snap
^^^^^^^^^^^

The object snap window controls, which object snap settings, are active.

User defined paper size
^^^^^^^^^^^^^^^^^^^^^^^

Object snap window
^^^^^^^^^^^^^^^^^^^^^^^

With the help of the user defined paper size function, customized paper
sizes can be created. As mentioned before, user defined formats are
independent from a printer.

In order to create user defined paper sizes, the page width and height
have to be chosen, as well as borders and folding marks.

User defined formats window

The new paper formats can be selected from, the paper size drop list in
the new view port window, if “Custom formats” are chosen for the
printing device.

Page layout
^^^^^^^^^^^

At first sight, the page layout window looks like the user defined
formats window. However, there are a few important differences. The
upper part provides the possibility to select the printing device and
the layout of the drawing. With the page layout function, it is possible
to change these paper settings later on, e.g. the paper size of a
finished drawing.

Page layout window

By using the “Save as default” button, the settings are saved as default
for the corresponding printing device.

Style settings
^^^^^^^^^^^^^^

In the following, it will be explained how to customize drawing,
dimension and text styles, as well as view port settings. Afterwards, it
is shown how to save these settings as a drawing template.

Drawing settings
^^^^^^^^^^^^^^^^

Objects, lines, circles, arcs and points will have the properties set in
the draw settings window. The color set, line type and line weight can
be selected in here.

-  Line type: Different line types are possible, such as continuous,
   dashed and dotted lines.
-  Line weight: The line weight is the thickness of a line when it is
   printed and is defined in the current unit system (meters).
-  Color set: The color set determines the color of the object.

If the properties are set to “by layer”, they are taken from the layer
settings and can be changed easily. Procedures to create and use
layers will be explained later on.

If different settings are selected here, the objects get their own
properties and have to be individually changed.

The properties of drawing objects can always be changed by right
clicking them and selecting “Edit properties” in the pop up menu.

Draw settings window

Dimension settings
------------------

This function allows creating and editing dimension style settings. The
current dimension style will be applied to any dimension created. If a
dimension style is edited, all the dimensions in the style will be
affected. For example, if the units of a dimension style are changed to
feet and inches, all the dimensions in that style will be changed to
feet and inches as well.

It is possible to set up dimension lines, angle dimensions, height
flags, a radius, diameter, and arc dimensions.

Dimension style window

Text settings
-------------

Text styles can be created and edited in the text settings window. The
current text style will be applied to any text created. If a text style
is edited, all the text in this style will be affected. For example, if
the color set of a text style is changed to green, all the text in that
style will be changed to green as well.

In the following section, two text styles will be created. One text
style will be used for general texts and the other one for title blocks.
The text style for title blocks will be defined as a table.

How to create title blocks will be explained later on.

-  Type 6 Text 🡪 1 Text style to create a new text style.

-  Click In the next empty space and select new setting and name it
   “Tutorial D‐CAD 2D”.

-  Select for the font “Georgia” and change the font size to
   “0.125”.(decimal for 1/8”)

-  Select for the line height “0,250” (decimal for ¼”) and for the color
   set “black”.

-  Click the “Save” button and afterwards the “Overwrite” button

-  .. rubric:: Create a new text style for the title block (table):
      :name: create-a-new-text-style-for-the-title-block-table

-  Click again in the next empty space and select new setting and name
   it “Tutorial D‐ CAD 2D – Title block”.

-  Take over the settings above.

-  Select for the first two table columns the width “=2” and for all
   line weights “0.0156”.(decimal for 1/64”)

-  The distance of the text to the column limits is “0.0781”(decimal for
   5/64”)

-  Click the “Save” button and afterwards the “Overwrite” button

-  Now the text style “Tutorial D‐CAD 2D – Title block” is in the
   database

-  Click “OK”.

Text style window

View port settings
------------------

View ports are spaces on paper that contain drawing objects. Each view
port has its own properties, such as scale, coordinate systems and
layers. For example, two view ports would be necessary, if two different
scales should be used.

With the view ports menu it is possible to create new view ports, to
change and to delete them.

In this example, it is necessary to create a new view port, as the
current window does not fit to the paper size.

In the following it is explained how to change the view port settings.

Layer
-----



Window settings window

Layers are like transparent sheets. Objects can be drawn on different
layers and they can be turned on and off. With the usage of layers, the
drawing can be organized.

Each layer has a number of properties, such as line type, line weight
and color set.

-  S: The tick S defines whether the layer is shown or hidden.
-  C: The tick C defines which layer is current. Only one layer can be
   current at a time.
-  Layer name: A new layer is added by entering a name.
-  Line type: Different line types are possible such as continuous,
   dashed and dotted lines.
-  Line weight: The line weight is the thickness of a line when it is
   printed and is defined in the current unit system (inch).

-  Color set: Each layer has a color set.

If the line type, line weight and color set (drawing settings) of an
object, that belongs to this layer, is set to “by layer”, it will be
indicated in the line type, line weight and color defined in here.

If the properties of a layer are changed, all lines will be changed
accordingly.

Layer window

How to create a title block
---------------------------

The following sections explain how to create title blocks with
customized labelling fields. In addition to that, a description of how
to insert pictures such as company logos will be provided.

The title block, which will be created in this tutorial, has three lines
and two columns and the overall size will be 10.0cm x 1.8cm. The
labelling fields as shown in the picture below will be created.

Title block

New view port:
--------------

First of all, a new view port has to be inserted, as title blocks should
be saved in their own view ports. Having its own view port, the title
block is independent from the drawing scale of the other view ports and
will always appear in the same size. It is recommended to use the scale
1/1 for this view port.

Window settings window

Text and keywords:
------------------

D-CAD-L 2D provides the possibility of using keywords. Keywords are
placeholders for drawing information, such as the project number and the
date of creation.

If the keywords are outdated, they can be updated by typing 6 Text 🡪 9
Update keywords.

Text window

Save title block to the library:
--------------------------------

Title blocks can be saved to the library in order to use them in other
drawings as well. The library is split up into two sections:

-  The first section contains drawing sections and will be explained
   later.
-          Drawing sections are objects that can be put into an existing
   view port such as furniture, people, cars and trees.
-  The second section contains view ports including their corresponding
   drawing objects, such as title blocks and entire drawings.

Library – view ports window

Import image:
-------------

This chapter explains how to insert pictures onto the drawing, such as
company logos. Supported files are EMF, WMF, PNG, BMP, JPEG, and GIF...

Import picture window

Imported picture size window

Images can be moved and deleted later on by typing 7 View ports 🡪 9
Image / RTF🡪 2 Move / 3 Delete.

Templates
---------

It is possible to save entire page layouts to drawing templates. These
templates can be used when creating new drawings.

The following settings are saved in templates:

-  Printing device
-  Paper size
-  View port orientation
-  Header
-  Drawing frame
-  View ports
-  Draw, text, dimension and view port settings
-  Layers
-  Drawing objects (e.g. title block)
-  Images

The picture below shows the current page layout, which will be saved as
a template.

Template page layout

Before the drawing is to be saved as a template, the main view port
should be set to the current one.

Save template window

Templates can be deleted be typing 1 File 🡪 3 Templates 🡪 3 Delete.

Finally, the drawing will be saved as a regular drawing.

How to draw with D-CAD-L 2D
---------------------------

The following chapters provide a step-by-step procedure for drawing with
D-CAD 2D. The first section focuses on how to draw and edit drawings and
the second part explains different options of dimensions. For Feet &
Inch input refer to page 85-87.

The following drawing of a carport will be drawn in the scale 1/35.

Drawing example

Draw and edit
-------------

First of all, a new drawing shall be started by using the new template.

.. _new-drawing-1:

New drawing
-----------

New drawing window

Edit text – title block
-----------------------

The title block has to be completed. Insert your name in the name field.

System variables window

Windows settings

Title block

Before starting to draw the carport, some functions to simplify the way
of drawing and to control the drawing will be explained.

Zoom in – zoom out
------------------

The left and right mouse buttons can be used to change the size of the
view area:

Zoom in: Click with the left mouse button to define the top left corner
and click again to define the right bottom corner of a zoom area.

Zoom out: Click the right mouse button to zoom out one step.

Click and drag the left mouse button to pan.

While a function is active, the mouse wheel cannot be used for zooming.
In this case, the “+” key can be used to zoom in and the “-” key to zoom
out.

Measuring
---------

The measurements of drawing objects can be checked by clicking either
the “middle mouse button” or “SHIFT” + “right mouse button”. There are
different possibilities to measure, such as “point to point” and “line”.

The measure window shows different measurements:

-  global coordinates of the starting and end points
-  distance between starting and end points
-  distances in X- and Y-direction of the end point related to the
   starting point
-  global angle to x-axis

By highlighting, a measurement and clicking copy copies it to clipboard.

Click the “measure” button to start another measurement or the “end”
button to stop measuring.

Measure window

Assistant menu
--------------

The “assistant menu” will be opened by clicking the “middle mouse
button” (or “SHIFT” + “right mouse button”) while a function is active.
The assistant menu provides a number of snap options.

How to use the assistant menu will be shown in the following instruction
manual.

Right mouse click – edit objects
--------------------------------

It is always possible to open an “edit menu” by highlighting a drawing
object, such as lines and texts, and clicking the “right mouse button”.

An object is highlighted by moving the crosshairs over the object. The
color of the object will change.

Now it is time to start to draw the drawing of the carport. The front
elevation of the carport will be drawn first.

Draw straight line
------------------

Front elevation – left post:
----------------------------

The first object, which will be drawn, is the left post in the front
elevation. It will be created by using the function “line”.

 The easiest way to draw straight lines is using the curser keys. The
window on the left will pop up. The direction can still be changed be

clicking on the direction button. The angle value to the right shows the
angle to the x-axis.

However, it is always possible to use the “left mouse button” to select
the end point of a line and to enter the correct coordinates in the pop
up window or to use the object snap function.

Draw box
--------

Right post:
-----------

The right post in the front elevation will be created by drawing a box.
For that purpose, two opposite points have to be selected by clicking
the “left mouse button”.

Reference point window

By typing the numbers, “1” to “5”, different input options can be chosen
to enter the end point:

#. Relative coordinates
#. Relative angle and length
#. Global coordinates
#. Global angle and length

--------------

Relative coordinates window

5. Angle to previous (the starting point and a reference line have to be
   selected before the dialog box appears).

current view - posts

Bottom plates:
--------------

The front views of the bottom plates on top of the posts are drawn with
the same

command. It is possible either to type 2 Draw 🡪 3 Lines 🡪 3
Box        again or to use the “+” key to repeat the last command.

Input option: relative coordinates window

Draw sloped line
----------------

Left rafter:
------------

The sloped top edge of the left rafter will be drawn with the function
“line”. The roof slope will be 30.256437° (which is equal to 7” / 12”)

                

Current view

Offset line
-----------

The roof overhang at the eave is obtained by offsetting the left line of
the top left plate in the distance of the eave overhang.

Offset window        Offset window

Current view, plate line offset

The line for the top edge of the rafter needs to be adjusted in length
to meet the line that was just offset.

Current view

The help line used to achieve the 1’ 8” overhang can now be deleted.

Current view

Current view – left rafter

Corner
------

Current view

Mirror
------

Right rafter:
-------------

The right rafter in the front elevation will be created by mirroring the
left one.

Assistant menu

Current view – right rafter

Ridge cutline:
--------------

Tie:

The tie in the front elevation will be drawn by drawing and offsetting
lines and using the assistant menu.

In the following, the bottom edge of the tie is drawn. The tie and the
bottom plate are connected by a lap joint. Therefore, there is an offset
between these members.

The top edge of the tie is created by offsetting the bottom edge 0.2m.

Copy
----

Ridge plate:
------------

The left bottom plate will be copied in order to create the ridge plate.

Number of copies

        

Delete:
-------

Tie post:

The last member to create in the front elevation is the tie post. The
function “line” will be used to draw it.

Current view – tie post

Trim and adjust lines
---------------------

The last step in constructing the front elevation is to adjust and trim
lines. That means lines will be cut and extended. The limits will always
be existing lines.

The location where the lines are clicked is important, because the lines
can be either cut or extended:

-  Function “adjust”:

With this function, it is possible to extend lines. Select a line as
limit. Click the end of the line, which shall be extended.

Function “adjust” - extension

It is also possible to cut lines with this function. Select a line as
limit. Click the line which shall be cut at the side which remains.

Function “adjust” – cut

-  Function “trim”:

This function cuts lines as well. Select a line as limit. Click the side
of the line, which shall be cut.

Function “trim” – cut

Trim tie to rafters:
----------------------------------

The function “Adjust” is used to cut lines. The top edge of the tie will
be cut at the rafter bottom lines.

Current view of the tie detail – function “adjust”

Trim ridge:
-----------

The function “trim” will be used to cut the rafter lines on the ridge
cut line.

Current view of the ridge detail        – function “trim”

Trim bird’s mouths:
-------------------

The bottom lines of the rafters have to be separated because of the
bird’s mouths.

Current view of the ridge bird’s mouths – function “trim”

Trim birds mouths at lower plates:
----------------------------------

Current view of the tie detail – function “trim”

The front elevation is finished. In the following section, the side
elevation will be created.

Side elevation – posts:
-----------------------

The posts in the side elevation will be copied from the front elevation.
In order to simplify the copying, the post in the side elevation will be
grouped.

Group objects
-------------

The group function groups objects, so that not every line has to be
selected in order to copy and move objects.

Here group is on, clicking on 5 now will turn it off.        Here the
opposite, clicking on 5 will turn it on.

Group mode on        Group mode off.

Posts:
------

The grouped post in the front elevation will be copied to the side
elevation.

Number of copies.        Direction + distance (length)

Bottom plate:
-------------


Current view – bottom plate

The bottom plate will be created by drawing the bottom line and
offsetting it 0.2m.

The top edge of the bottom plate is drawn by offsetting the bottom line.

.. _ridge-plate-1:

Ridge plate:
------------

The ridge plate is copied from the bottom plate.

Direction        Measure

        

Measure results        Direction (copied distance)

Tie:
----



Current view – ridge plate

The left tie and tie post will be drawn first and the middle and right
ones will be created by using the function “copy”.

The function “box” is used to draw the front view of the tie.

Tie post:
---------

Draw two vertical lines to create the tie post.

Current view – tie and tie post

The middle and right ties and tie posts are created by copying the left
one.

The top edge of the bottom plate has to be trimmed by the ties.

.. _left-rafter-1:

Left rafter:
------------



Current view – copied tie and tie posts

The left rafter will be created by projecting lines from the front view
to the side view. These construction lines have to be trimmed later. The
other rafters will be copied from the left one.

First, the construction lines will be drawn.

Current view – construction lines of the left rafter

Draw the left edge of the left rafter.

Create the right rafter line by offsetting the left one.

Current view – left rafter lines

Adjust the lines of the left rafter.

Trim the construction lines.

Current view – adjusted rafter lines

Rafters:
--------

The other rafters will be copied from the left one. Group all lines of
the left rafter in order to copy it easier.

Use the function “copy”.

-  Type 3 Edit 🡪 1 Copy        .
-  Select the left rafter.
-  Right click insert “9” for number of copies then click Ok. Point of
   origin:
-  Select the intersection where the right side of the rafter meets the
   bottom of the bottom plate.

Point of destination:

-  Use the curser key right to select the direction – “🡪”.
-  Use the measure icon in the direction dialog box and click “point –
   point”
-  Select for the first point the same point you chose for origin and
   the right end of the bottom plate for the second point.
-  In the next measure dialog box highlight the measurement “distance in
   X‐ direction” then type “+” and the calculator will open
   automatically.
-  Replace the “+” with “÷9” and press enter.
-  Again, highlight “Distance in x direction” and press “copy”.
-  The dimension will be in the direction dialog box now press the
   “enter key”.
-  Click the “right mouse button” two times to quit the command.

Chose point        measure icon

        

Measure point – point        distance in X – direction

Using calculator function

Calculated distance        Distance in 🡪

Current view – copied rafters

Wall brace:
-----------

In the following, methods for drawing wall braces with arcs will be
explained.

The wall brace created in this tutorial will be saved to the library in
order to insert it easier on other positions and to use it in other
drawings as well.

First, straight lines will be drawn and afterwards the arc will be
created.

Offset the line to get the top edge of the wall brace.

Current view – wall brace

Draw arc
--------

The arc of the wall brace is created by selecting the starting and end
point and choosing the height of the arc.

Arc segment height.

Current view – arc

Delete line
-----------

There are different possibilities to delete lines:

-  .. rubric:: 3 Edit 🡪 08 Delete
      :name: edit-08-delete

🡪 This command deletes all objects, such as grouped objects, lines,
texts, dimensions, points, circles, arcs, and height flags.

-  .. rubric:: 2 Draw 🡪 8 Delete
      :name: draw-8-delete

🡪 This command deletes only single lines, such as lines, circles and
arcs and points.

The straight lower line of the wall brace has to be deleted.

Trim the upper line of the wall brace.

Current view – finished left wall brace

Connect the ends of the upper and lower wall brace line. These lines
will not be seen but they are necessary to position the wall brace from
the library.

Library
-------

It is possible to save drawing objects in the library in order to copy
them and to use them in other drawings as well.

The library is split up into two sections:

-  The first section contains drawing sections. Drawing sections are
   objects that can be put into an existing view port, such as
   furniture, people, cars and trees and in this example a wall brace.
-  The second section was already explained earlier when the title block
   was saved and contains view ports including their corresponding
   drawing objects, such as title blocks and entire drawings.

In the following, the wall brace will be saved to the library.

Library – drawing sections window

By clicking the “read” button, the drawing section can be inserted.

Current view – all wall braces

The lines of the wall braces and plates have to be trimmed by the
rafters.

Current view – trimmed lines

Hatching
--------

All plates, ties and rafter front views will be hatched with the
hatching “end grain”.

Current view - hatching

Text
----

Finally, a single line text will be added to describe each elevation.

Single line text

Current view – single line text


