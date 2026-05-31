# Chess_game 
## Có trong bản này

- GameState dataclass sạch
- Timer thống nhất
- Castling chuẩn
- En passant
- Promotion UI
- Check / Checkmate / Stalemate
- FEN import/export module
- PGN export module
- Save / Load JSON
- Theme system
- Resource cache ảnh quân cờ
- Sidebar 
- Move history
- Màn hình cài đặt thời gian trước khi bắt đầu ván.
- Mở rộng unit test
- PGN nâng cao
- Replay ván đấu
- Validator tối ưu
- Thông báo lỗi trực quan khi load save thất bại.

## Cách chạy

pip install pygame-ce
python main.py

## Phím tắt

- R: Reset
- S: Lưu Ván Cờ
- L: Load Lại Ván Trước
- T: Đổi Chủ Đề
- P: Xuất PGN
- V: Bắt đầu replay
- ← / →: Lùi / tiến trong replay
- END hoặc ESC: Thoát replay

## Assets

Cần có ảnh quân cờ trong `assets/`:

wP.png wR.png wN.png wB.png wQ.png wK.png
bP.png bR.png bN.png bB.png bQ.png bK.png

## Tác Giả

Lê Minh Hưng
MSSV: 3025102193