# パスワード管理アプリケーション

## 概要
このアプリケーションは、安全にパスワードを管理するためのPython製のGUIツールです。Fernetによる強力な暗号化を使用し、ユーザーインターフェースは日本語、英語、中国語に対応しています。

## 特徴
- パスワードの安全な暗号化と保存
- サービス名によるパスワードの取得
- 強力なパスワードの自動生成
- パスワードの編集と削除機能
- 全パスワードの一覧表示
- パスワードの強度チェック
- データのエクスポートとインポート機能
- 日本語、英語、中国語に対応したユーザーインターフェース
- マスターパスワードによるセキュリティ保護

## 必要条件
- Python 3.6以上
- cryptographyライブラリ

## インストール方法
1. このリポジトリをクローンまたはダウンロードします。
2. 必要なライブラリをインストールします：
   ```
   pip install cryptography
   ```

## 使用方法
1. 以下のコマンドでアプリケーションを実行します：
   ```
   python main.py
   ```
2. GUIウィンドウが開きます。
3. 上部の言語選択メニューから希望の言語を選択します。
4. マスターパスワードを設定または入力します。
5. サービス名、ユーザー名、パスワードを入力し、「追加」ボタンをクリックしてパスワードを保存します。
6. 保存したパスワードを取得するには、サービス名を入力し「取得」ボタンをクリックします。
7. 新しいパスワードを生成するには「生成」ボタンをクリックします。
8. パスワードを編集または削除するには、対応するボタンを使用します。
9. 全てのパスワードを表示するには「一覧表示」ボタンをクリックします。
10. データのエクスポートとインポートには、対応するボタンを使用します。

## ファイル構成
- `main.py`: アプリケーションのエントリーポイント
- `password_manager.py`: パスワード管理の核となる機能を提供
- `gui.py`: グラフィカルユーザーインターフェースを実装
- `translations.py`: 多言語サポートのための翻訳を管理
- `utils.py`: パスワードの強度チェックなどのユーティリティ関数を提供

## セキュリティについて
- このアプリケーションはFernet暗号化を使用してパスワードを保護しています。
- マスターパスワードは適切に保護し、忘れないようにしてください。マスターパスワードを失うと、保存したすべてのパスワードにアクセスできなくなります。
- このツールは個人使用を目的としています。重要な情報の管理には、さらに高度なセキュリティ対策を施したツールの使用を検討してください。

---

# Password Manager Application

## Overview
This application is a Python-based GUI tool for securely managing passwords. It uses strong Fernet encryption and supports user interfaces in Japanese, English, and Chinese.

## Features
- Secure encryption and storage of passwords
- Password retrieval by service name
- Automatic generation of strong passwords
- Password editing and deletion functionality
- Display of all stored passwords
- Password strength checker
- Data export and import functionality
- User interface available in Japanese, English, and Chinese
- Security protection with a master password

## Requirements
- Python 3.6 or higher
- cryptography library

## Installation
1. Clone or download this repository.
2. Install the required library:
   ```
   pip install cryptography
   ```

## Usage
1. Run the application with the following command:
   ```
   python main.py
   ```
2. The GUI window will open.
3. Select your preferred language from the language selection menu at the top.
4. Set or enter your master password.
5. Enter the service name, username, and password, then click the "Add" button to save the password.
6. To retrieve a saved password, enter the service name and click the "Get" button.
7. Click the "Generate" button to create a new strong password.
8. Use the corresponding buttons to edit or delete passwords.
9. Click the "List All" button to display all stored passwords.
10. Use the corresponding buttons for data export and import.

## File Structure
- `main.py`: Entry point of the application
- `password_manager.py`: Provides core password management functionality
- `gui.py`: Implements the graphical user interface
- `translations.py`: Manages translations for multi-language support
- `utils.py`: Provides utility functions such as password strength checking

## Security Notes
- This application uses Fernet encryption to protect your passwords.
- Keep your master password secure and don't forget it. If you lose your master password, you won't be able to access any of your stored passwords.
- This tool is intended for personal use. For managing highly sensitive information, consider using tools with more advanced security measures.

<img src="">

## **作成者 Developer**

- 作成者: xM1guel
- GitHub: https://github.com/xM1guel
- Zenn: https://zenn.dev/miguel
