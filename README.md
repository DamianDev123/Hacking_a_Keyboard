# Orpheuspad

Orpheuspad is a 4 key macropad with a rotary encoder, OLED display, and WS2812B LEDs. It runs QMK firmware and serves as a reference implementation for the Hackpad YSWS, demonstrating a full set of common macropad features.

It acts as both a functional device and a design reference for future hackpad-style projects.

---

## Features:
- 128×32 OLED display
- 4× WS2812B RGB LEDs
- 9 keys
---

## CAD Model:
Everything fits together using 6 M3 bolts and heat-set inserts:
- 4 for the case
- 2 for securing the PCB

It consists of 3 printed parts:
- Bottom case
- Top cover
<img width="500" alt="Screenshot 2026-06-29 at 7 42 36 AM" src="https://github.com/user-attachments/assets/48a60acc-b31f-4020-a1d1-e1f9525ba796" />


Made in Onshape.

---

## PCB:
Designed in KiCad with silkscreen imported from Figma.

Schematic:
<img width="300" alt="Screenshot 2026-06-29 at 8 33 09 AM" src="https://github.com/user-attachments/assets/933b5d8c-a4d2-4527-a1f2-f6e119dcf03c" />

PCB:
<img width="315" height="273" alt="Screenshot 2026-06-29 at 8 32 51 AM" src="https://github.com/user-attachments/assets/4c265c80-e79d-40e8-99fa-103e1bbcdd90" />
---

## Firmware Overview:
This hackpad uses KMK firmware.

- 9 keys:
  - randoms keys

- RGB:
  - Gaming
    
- OLED display:
  - TODO

More features may be added later.

---

## BOM:
Everything needed to build the hackpad:

- 9× Cherry MX switches
- 9× DSA keycaps
- 4× M3×5×4 heat-set inserts
- 6× M3×16 SHCS bolts
- 9× 1N4148 DO-35 diodes
- 4× WS2812B LEDs
- 1× 0.91" 128×32 OLED display
- 1× Seeed XIAO RP2040
- 1× case (2 printed parts)
