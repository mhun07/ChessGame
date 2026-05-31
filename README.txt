# ♟️ ĐỒ ÁN TRÒ CHƠI CỜ VUA

Ứng dụng trò chơi cờ vua được phát triển bằng **Python** và thư viện **pygame-ce**, mô phỏng đầy đủ luật chơi cờ vua truyền thống cùng giao diện đồ họa trực quan và thân thiện với người dùng.

---

# 📌 Giới Thiệu

Đây là đồ án môn học được xây dựng nhằm áp dụng các kiến thức đã học về:

* Lập trình Python
* Lập trình hướng đối tượng (Object-Oriented Programming)
* Thiết kế giao diện đồ họa
* Quản lý trạng thái chương trình
* Cấu trúc dữ liệu và giải thuật
* Quản lý mã nguồn bằng Git & GitHub

Ứng dụng cho phép hai người chơi tham gia một ván cờ vua hoàn chỉnh với đầy đủ các luật chơi cơ bản và nâng cao.

---

# 🎯 Mục Tiêu Đề Tài

* Xây dựng trò chơi cờ vua bằng Python.
* Áp dụng mô hình lập trình hướng đối tượng.
* Tạo giao diện đồ họa trực quan bằng pygame-ce.
* Hiện thực đầy đủ các luật của cờ vua.
* Tổ chức mã nguồn theo cấu trúc module rõ ràng.
* Nâng cao kỹ năng thiết kế phần mềm và phát triển ứng dụng.

---

# ✨ Chức Năng Chính

## ♜ Luật Chơi Cờ Vua

* Di chuyển quân cờ đúng luật
* Kiểm tra nước đi hợp lệ
* Chiếu vua (Check)
* Chiếu hết (Checkmate)
* Hòa cờ (Stalemate)
* Nhập thành (Castling)
* Phong cấp Tốt (Pawn Promotion)
* Bắt tốt qua đường (En Passant)
* Ghi nhận lịch sử nước đi

## 🎮 Giao Diện Người Dùng

* Bàn cờ đồ họa trực quan
* Hiển thị lượt chơi
* Hiển thị trạng thái trận đấu
* Đánh dấu quân cờ đang được chọn
* Hiển thị các nước đi hợp lệ
* Hiển thị thông báo kết thúc trận đấu

## 💾 Quản Lý Trận Đấu

* Bắt đầu ván mới
* Lưu trận đấu
* Tải trận đấu đã lưu
* Chơi lại từ đầu
* Hoàn tác nước đi
* Theo dõi lịch sử trận đấu

---

# 🛠 Công Nghệ Sử Dụng

| Công nghệ  | Mô tả                                |
| ---------- | ------------------------------------ |
| Python 3.x | Ngôn ngữ lập trình chính             |
| pygame-ce  | Xây dựng giao diện và xử lý trò chơi |
| OOP        | Lập trình hướng đối tượng            |
| JSON       | Lưu trữ dữ liệu trận đấu             |
| Git        | Quản lý mã nguồn                     |
| GitHub     | Lưu trữ và chia sẻ dự án             |

---

# 📂 Cấu Trúc Dự Án

```text
ChessGame/
│
├── assets/          # Hình ảnh, biểu tượng và tài nguyên
├── core/            # Các lớp dữ liệu chính
├── engine/          # Xử lý luật chơi cờ vua
├── render/          # Hiển thị giao diện
├── saves/           # Dữ liệu lưu trận đấu
├── tests/           # Kiểm thử chương trình
├── ui/              # Thành phần giao diện người dùng
├── utils/           # Các hàm hỗ trợ
│
├── main.py          # Điểm khởi chạy chương trình
├── requirements.txt
├── README.md
└── .gitignore
```

---

# 🚀 Hướng Dẫn Cài Đặt

## 1. Clone dự án

```bash
git clone https://github.com/mhun07/ChessGame.git
```

## 2. Di chuyển vào thư mục dự án

```bash
cd ChessGame
```

## 3. Tạo môi trường ảo

```bash
python -m venv .venv
```

## 4. Kích hoạt môi trường ảo

Windows:

```bash
.venv\Scripts\activate
```

Linux/macOS:

```bash
source .venv/bin/activate
```

## 5. Cài đặt thư viện

```bash
pip install -r requirements.txt
```

---

# ▶️ Chạy Chương Trình

```bash
python main.py
```

---

# 🎮 Hướng Dẫn Sử Dụng

| Thao tác   | Chức năng         |
| ---------- | ----------------- |
| Chuột trái | Chọn quân cờ      |
| Chuột trái | Di chuyển quân cờ |
| New Game   | Tạo ván mới       |
| Save Game  | Lưu trận đấu      |
| Load Game  | Tải trận đấu      |
| Undo       | Hoàn tác nước đi  |

---

# 🏗 Kiến Trúc Hệ Thống

### Engine Layer

Xử lý toàn bộ luật chơi cờ vua:

* Kiểm tra nước đi hợp lệ
* Chiếu vua
* Chiếu hết
* Hòa cờ
* Phong cấp

### Core Layer

Quản lý dữ liệu:

* Bàn cờ
* Quân cờ
* Trạng thái trò chơi
* Lịch sử nước đi

### Render Layer

Chịu trách nhiệm:

* Vẽ bàn cờ
* Hiển thị quân cờ
* Hiển thị hiệu ứng giao diện

### UI Layer

Xử lý:

* Sự kiện chuột
* Nút chức năng
* Menu và thông báo

### Utility Layer

Chứa các hàm hỗ trợ được sử dụng chung trong toàn bộ dự án.

---

# 📚 Kiến Thức Áp Dụng

Thông qua đồ án này, các kiến thức sau đã được vận dụng:

* Lập trình hướng đối tượng (OOP)
* Quản lý trạng thái chương trình
* Xử lý sự kiện trong pygame-ce
* Thiết kế giao diện đồ họa
* Tổ chức dự án theo mô hình module
* Quản lý mã nguồn bằng Git
* Làm việc với dữ liệu JSON

---

# 📸 Hình Ảnh Minh Họa

Có thể bổ sung ảnh chụp màn hình chương trình tại đây:

```markdown
![Menu](screenshots/menu.png)

![Gameplay](screenshots/gameplay.png)

![Checkmate](screenshots/checkmate.png)
```

---

# 👨‍💻 Thông Tin Sinh Viên

**Họ và tên:** Lê Minh Hùng

**MSSV:** 3025102193

**Môn học:** Lập Trình Python

**GitHub:** https://github.com/mhun07

---

# 📄 Giấy Phép

Dự án được phát triển phục vụ mục đích học tập, nghiên cứu và báo cáo môn học.
