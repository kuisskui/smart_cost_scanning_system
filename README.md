# Excel Price Processor (ระบบหาราคาสินค้าอัจฉริยะ)

A Python application for processing and comparing product prices from Excel files. This application helps users manage and analyze product pricing data efficiently with a modern GUI interface.

## Features

- Modern GUI interface built with CustomTkinter
- Excel file processing for product pricing data
- Historical price comparison
- Real-time progress tracking
- Thai language support
- Easy-to-use file selection and processing
- Date-based price comparison

## Requirements

- Python 3.8 or higher
- Dependencies listed in `requirements.txt`

## Installation

1. Clone the repository:
```bash
git clone https://github.com/kuisskui/smart_cost_scanning_system.git
cd smart_cost_scanning_system
```

2. Create a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

1. Run the application:
```bash
python main.py
```

2. Using the application:
   - Select the history file ("ประวัติการซื้อสินค้า")
   - Select the orders file ("รายการสินค้า")
   - Enter the date for price comparison (optional)
   - Click "ประมวลผล" to process the files
   - Monitor the progress bar
   - Download the results when processing is complete

## File Format Requirements

### History File ("ประวัติการซื้อสินค้า")
- Must be an Excel file (.xlsx)
- Sheet name: "บริษัท, ร้านค้า"
- Required columns:
  - po_no
  - start_date
  - end_date
  - company_name
  - order_name
  - amount
  - unit
  - price
  - total
  - price_vat
  - total_vat

### Orders File ("รายการสินค้า")
- Must be an Excel file (.xlsx)
- Sheet name: "วัตถุดิบ"
- Same column structure as the history file

## Project Structure

```
excel-price-processor/
├── main.py              # Application entry point
├── src/
│   ├── gui.py          # Main GUI implementation
│   ├── services/       # Business logic services
│   │   └── processer_excel.py
│   └── frame/         # GUI components
├── requirements.txt    # Project dependencies
└── README.md          # This file
```
