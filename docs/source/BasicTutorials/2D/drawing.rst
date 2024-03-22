FF - How to draw with D-CAD-L 2D
--------------------------------

The following chapters provide a step-by-step procedure for drawing with
D-CAD 2D. The first section focuses on how to draw and edit drawings and
the second part explains different options of dimensions. For Feet &
Inch input refer to page 85-87.

The following drawing of a carport will be drawn in the scale 1/35.

Drawing example

Draw and edit
^^^^^^^^^^^^^

First of all, a new drawing shall be started by using the new template.

.. _new-drawing-1:

New drawing
^^^^^^^^^^^^^


New drawing window

Edit text – title block
^^^^^^^^^^^^^^^^^^^^^^^

The title block has to be completed. Insert your name in the name field.

System variables window

Windows settings

Title block

Before starting to draw the carport, some functions to simplify the way
of drawing and to control the drawing will be explained.

Zoom in – zoom out
^^^^^^^^^^^^^^^^^^


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
^^^^^^^^^


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
^^^^^^^^^^^^^^


The “assistant menu” will be opened by clicking the “middle mouse
button” (or “SHIFT” + “right mouse button”) while a function is active.
The assistant menu provides a number of snap options.

How to use the assistant menu will be shown in the following instruction
manual.

Right mouse click – edit objects
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

It is always possible to open an “edit menu” by highlighting a drawing
object, such as lines and texts, and clicking the “right mouse button”.

An object is highlighted by moving the crosshairs over the object. The
color of the object will change.

Now it is time to start to draw the drawing of the carport. The front
elevation of the carport will be drawn first.

Draw straight line
^^^^^^^^^^^^^^^^^^


Front elevation – left post:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^


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
^^^^^^^^


Right post:
^^^^^^^^^^^


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


Relative coordinates window

5. Angle to previous (the starting point and a reference line have to be
   selected before the dialog box appears).

current view - posts

Bottom plates:
^^^^^^^^^^^^^^

The front views of the bottom plates on top of the posts are drawn with
the same

command. It is possible either to type 2 Draw 🡪 3 Lines 🡪 3
Box        again or to use the “+” key to repeat the last command.

Input option: relative coordinates window

Draw sloped line
^^^^^^^^^^^^^^^^


Left rafter:
^^^^^^^^^^^^^


The sloped top edge of the left rafter will be drawn with the function
“line”. The roof slope will be 30.256437° (which is equal to 7” / 12”)

                

Current view

Offset line
^^^^^^^^^^^^^


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
^^^^^^


Current view

Mirror
^^^^^^


Right rafter:
^^^^^^^^^^^^^


The right rafter in the front elevation will be created by mirroring the
left one.

Assistant menu

Current view – right rafter

Ridge cutline:
^^^^^^^^^^^^^^


Tie:

The tie in the front elevation will be drawn by drawing and offsetting
lines and using the assistant menu.

In the following, the bottom edge of the tie is drawn. The tie and the
bottom plate are connected by a lap joint. Therefore, there is an offset
between these members.

The top edge of the tie is created by offsetting the bottom edge 0.2m.

Copy
^^^^


Ridge plate:
^^^^^^^^^^^^


The left bottom plate will be copied in order to create the ridge plate.

Number of copies

        

Delete:
^^^^^^^


Tie post:

The last member to create in the front elevation is the tie post. The
function “line” will be used to draw it.

Current view – tie post

Trim and adjust lines
^^^^^^^^^^^^^^^^^^^^^


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
^^^^^^^^^^^^^^^^^^^^


The function “Adjust” is used to cut lines. The top edge of the tie will
be cut at the rafter bottom lines.

Current view of the tie detail – function “adjust”

Trim ridge:
^^^^^^^^^^^


The function “trim” will be used to cut the rafter lines on the ridge
cut line.

Current view of the ridge detail        – function “trim”

Trim bird’s mouths:
^^^^^^^^^^^^^^^^^^^


The bottom lines of the rafters have to be separated because of the
bird’s mouths.

Current view of the ridge bird’s mouths – function “trim”

Trim birds mouths at lower plates:
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^



Current view of the tie detail – function “trim”

The front elevation is finished. In the following section, the side
elevation will be created.

Side elevation – posts:
^^^^^^^^^^^^^^^^^^^^^^^



The posts in the side elevation will be copied from the front elevation.
In order to simplify the copying, the post in the side elevation will be
grouped.

Group objects
^^^^^^^^^^^^^


The group function groups objects, so that not every line has to be
selected in order to copy and move objects.

Here group is on, clicking on 5 now will turn it off.        Here the
opposite, clicking on 5 will turn it on.

Group mode on        Group mode off.

Posts:
^^^^^^


The grouped post in the front elevation will be copied to the side
elevation.

Number of copies.        Direction + distance (length)

Bottom plate:
^^^^^^^^^^^^^



Current view – bottom plate

The bottom plate will be created by drawing the bottom line and
offsetting it 0.2m.

The top edge of the bottom plate is drawn by offsetting the bottom line.

.. _ridge-plate-1:

Ridge plate:
^^^^^^^^^^^^^


The ridge plate is copied from the bottom plate.

Direction        Measure

        

Measure results        Direction (copied distance)

Tie:
^^^^^^^^^^^^^





Current view – ridge plate

The left tie and tie post will be drawn first and the middle and right
ones will be created by using the function “copy”.

The function “box” is used to draw the front view of the tie.

Tie post:
^^^^^^^^^^^^^


Draw two vertical lines to create the tie post.

Current view – tie and tie post

The middle and right ties and tie posts are created by copying the left
one.

The top edge of the bottom plate has to be trimmed by the ties.

.. _left-rafter-1:

Left rafter:
^^^^^^^^^^^^^




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
^^^^^^^^^^^^^


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
^^^^^^^^^^^^^


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
^^^^^^^^^^^^^


The arc of the wall brace is created by selecting the starting and end
point and choosing the height of the arc.

Arc segment height.

Current view – arc

Delete line
^^^^^^^^^^^^^


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
^^^^^^^^^^^^^


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
^^^^^^^^


All plates, ties and rafter front views will be hatched with the
hatching “end grain”.

Current view - hatching

Text
^^^^


Finally, a single line text will be added to describe each elevation.

Single line text

Current view – single line text


