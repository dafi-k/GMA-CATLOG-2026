#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import json

# Read the CSV file and extract product data
products = []

with open('GMA/GMA_Catalog_50_Products.xlsx - קטלוג 50 מוצרים.csv', 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        product = {
            'code': row['קוד מוצר'],
            'name': row['שם המוצר'],
            'description': row['תיאור קצר'],
            'price': row['מחיר מכירה (₪)'],
            'category': row['קטגוריה'],
            'image': f"GMA/PIC/{row['קוד מוצר']}.avif"
        }
        products.append(product)

# Create HTML file
html_content = '''<!DOCTYPE html>
<html lang="he" dir="rtl">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>קטלוג מוצרים GMA</title>
    <link href="https://fonts.googleapis.com/css2?family=Heebo:wght@400;500;700;800&display=swap" rel="stylesheet">
    <style>
        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }

        body {
            font-family: 'Heebo', sans-serif;
            background: linear-gradient(135deg, #f5f7fa 0%, #ffffff 100%);
            padding: 40px 20px;
            min-height: 100vh;
        }

        .container {
            max-width: 1400px;
            margin: 0 auto;
        }

        .header {
            text-align: center;
            margin-bottom: 50px;
            animation: slideDown 0.6s ease-out;
        }

        .header h1 {
            font-size: 3em;
            color: #1e3a8a;
            margin-bottom: 10px;
            font-weight: 800;
            letter-spacing: -1px;
        }

        .header p {
            font-size: 1.1em;
            color: #6b7280;
            font-weight: 500;
        }

        .products-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(320px, 1fr));
            gap: 30px;
            animation: fadeIn 0.8s ease-out;
        }

        @media (min-width: 768px) {
            .products-grid {
                grid-template-columns: repeat(3, 1fr);
            }
        }

        @media (max-width: 768px) {
            .products-grid {
                grid-template-columns: 1fr;
            }

            .header h1 {
                font-size: 2em;
            }
        }

        .product-card {
            background: white;
            border-radius: 16px;
            overflow: hidden;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.07), 0 10px 20px rgba(0, 0, 0, 0.05);
            transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1);
            display: flex;
            flex-direction: column;
            height: 100%;
        }

        .product-card:hover {
            transform: translateY(-8px);
            box-shadow: 0 12px 24px rgba(0, 0, 0, 0.15), 0 20px 40px rgba(0, 0, 0, 0.1);
        }

        .product-image {
            width: 100%;
            height: 280px;
            object-fit: cover;
            background: linear-gradient(135deg, #e5e7eb 0%, #f3f4f6 100%);
        }

        .product-content {
            padding: 24px;
            flex: 1;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }

        .product-code {
            font-size: 0.85em;
            color: #0ea5e9;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 1px;
            margin-bottom: 8px;
        }

        .product-name {
            font-size: 1.3em;
            color: #1f2937;
            font-weight: 700;
            margin-bottom: 12px;
            line-height: 1.4;
            min-height: 2.8em;
        }

        .product-description {
            font-size: 0.95em;
            color: #6b7280;
            margin-bottom: 16px;
            line-height: 1.6;
            min-height: 2.4em;
            flex-grow: 1;
        }

        .product-footer {
            display: flex;
            justify-content: space-between;
            align-items: center;
            margin-top: 16px;
            padding-top: 16px;
            border-top: 1px solid #e5e7eb;
        }

        .product-price {
            font-size: 1.8em;
            color: #1e3a8a;
            font-weight: 800;
        }

        .product-price .currency {
            font-size: 0.8em;
            margin-left: 4px;
        }

        .btn-request {
            background: linear-gradient(135deg, #1e3a8a 0%, #2563eb 100%);
            color: white;
            border: none;
            padding: 12px 20px;
            border-radius: 8px;
            font-size: 0.95em;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.3s ease;
            font-family: 'Heebo', sans-serif;
            white-space: nowrap;
        }

        .btn-request:hover {
            background: linear-gradient(135deg, #1e40af 0%, #1d4ed8 100%);
            transform: translateX(-2px);
            box-shadow: 0 8px 16px rgba(30, 58, 138, 0.3);
        }

        .btn-request:active {
            transform: translateX(0);
        }

        @keyframes slideDown {
            from {
                opacity: 0;
                transform: translateY(-20px);
            }
            to {
                opacity: 1;
                transform: translateY(0);
            }
        }

        @keyframes fadeIn {
            from {
                opacity: 0;
            }
            to {
                opacity: 1;
            }
        }

        .product-card {
            animation: fadeIn 0.5s ease-out;
        }

        .product-card:nth-child(1) { animation-delay: 0.05s; }
        .product-card:nth-child(2) { animation-delay: 0.1s; }
        .product-card:nth-child(3) { animation-delay: 0.15s; }
        .product-card:nth-child(4) { animation-delay: 0.2s; }
        .product-card:nth-child(5) { animation-delay: 0.25s; }
        .product-card:nth-child(n+6) { animation-delay: 0.3s; }

        /* Category badge */
        .product-category {
            display: inline-block;
            font-size: 0.75em;
            background: #e0e7ff;
            color: #1e40af;
            padding: 4px 12px;
            border-radius: 20px;
            margin-bottom: 12px;
            font-weight: 600;
        }
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>🎁 קטלוג מוצרים GMA</h1>
            <p>מוצרים חדשים וחדשניים לבחירה</p>
        </div>

        <div class="products-grid" id="productsGrid">
            <!-- Products will be inserted here -->
        </div>
    </div>

    <script>
        const products = ''' + json.dumps(products, ensure_ascii=False) + ''';

        function renderProducts() {
            const grid = document.getElementById('productsGrid');
            grid.innerHTML = products.map(product => `
                <div class="product-card">
                    <img src="${product.image}" alt="${product.name}" class="product-image" onerror="this.src='data:image/svg+xml,%3Csvg xmlns=%22http://www.w3.org/2000/svg%22 width=%22320%22 height=%22280%22%3E%3Crect fill=%22%23e5e7eb%22 width=%22320%22 height=%22280%22/%3E%3Ctext x=%2250%25%22 y=%2250%25%22 font-family=%22Arial%22 font-size=%2216%22 fill=%22%236b7280%22 text-anchor=%22middle%22 dominant-baseline=%22middle%22%3Eתמונה לא זמינה%3C/text%3E%3C/svg%3E'">
                    <div class="product-content">
                        <div>
                            <div class="product-code">${product.code}</div>
                            <div class="product-category">${product.category}</div>
                            <h2 class="product-name">${product.name}</h2>
                            <p class="product-description">${product.description}</p>
                        </div>
                        <div class="product-footer">
                            <div class="product-price">
                                ${product.price}<span class="currency">₪</span>
                            </div>
                            <button class="btn-request" onclick="requestProduct('${product.code}', '${product.name}')">שלח בקשה</button>
                        </div>
                    </div>
                </div>
            `).join('');
        }

        function requestProduct(code, name) {
            alert(`בקשה לממלא: \\nקוד מוצר: ${code}\\nשם המוצר: ${name}`);
            // You can replace this with an actual form submission
        }

        // Render products on page load
        document.addEventListener('DOMContentLoaded', renderProducts);
    </script>
</body>
</html>
'''

# Write HTML file
with open('catalog.html', 'w', encoding='utf-8') as f:
    f.write(html_content)

print("✅ קובץ catalog.html נוצר בהצלחה!")
print(f"📦 סה״כ {len(products)} מוצרים")
