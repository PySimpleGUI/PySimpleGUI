## `Push` and `VPush` Elements For Justification

The aliases `Push` and `VPush` are aliases for `Stretch` and `VStretch`. `Stetch`, `VStretch`, and `Push` was in the 4.48.0 release.  `VPush` will be in the 4.49.0 release. 

There are a couple of new Elements that help with layout justification (functions that act like elements to be precise).

`Push` will push elements in a row away from it.  If you have a row with a `Push` element on the left, then it will push the elements to the right of it to the right.  If you have one on each end of a row, then the result will be the elements between them will be centered.

`VPush` pushes rows of elements vertically in the same fashion that the `Push` does horizontally.  Place a `VPush` on the first row and it will push the other rows to the very bottom of the container (e.g. window).

This example centers a couple of elements in the middle of the window by surrounding them by `Push` and `VPush` elements.


<iframe src='https://trinket.io/embed/pygame/752555630c?start=result' width='100%' height='500' frameborder='0' marginwidth='0' marginheight='0' allowfullscreen></iframe>
