# mag_stripe

The most basic of card readers.  
Collect Single Track Magnetic stripe card data so my hands dontdogo raw typing in long strings.
Parse for the card number.

## TODO
- [ ] do a lookup and add to sheet as the original (and current) balance in RPOS
- [ ] devise a tracking sheet for assignment of cards and distributing them
- [ ] Package as an EXE so someone else can do this in the future and thye dont need to go through the pain I had to of reading crumpled manually pencilled numbers.
- [ ] Investigate pywinusb to identify devices and capture read/end read events so that the user does not need to manually confrim entry of each card.
  - but really who cares - this isnt used very much. :)
