import os
from inventory import Inventory
from product import Electronics, Grocery, Clothing
from exceptions import *
from time import sleep

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def loading_animation(message):
    for _ in range(3):
        print(f"\r{message}", end="")
        for i in range(3):
            sleep(0.3)
            print(".", end="", flush=True)
        sleep(0.3)
    print()

def display_banner():
    print("\n" + "="*60)
    print("🌟 Welcome to Advanced Inventory Management System 🌟".center(60))
    print("="*60)

def main():
    inv = Inventory()

    while True:
        clear_screen()
        display_banner()
        print("\n🎯 Main Menu:")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
        print("✨ 1. Add New Product")
        print("💰 2. Sell Product")
        print("🔍 3. Search Product")
        print("📋 4. View All Products")
        print("💾 5. Save Inventory")
        print("📂 6. Load Inventory")
        print("📊 7. Inventory Statistics")
        print("🔄 8. Update Product")
        print("❌ 9. Delete Product")
        print("🚪 10. Exit")
        print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

        choice = input("\n👉 Please choose an option (1-10): ")

        try:
            if choice == "1":
                clear_screen()
                print("\n🌟 === Add New Product === 🌟")
                print("━━━━━━━━━━━━━━━━━━━━━━━━━")
                p_type = input("📦 Enter product type:\n1. Electronics\n2. Grocery\n3. Clothing\nChoice (1-3): ")
                pid = input("🔢 Product ID: ")
                name = input("📝 Product Name: ")
                price = float(input("💲 Price: $"))
                qty = int(input("📊 Quantity: "))

                if p_type == "1":
                    brand = input("🏢 Brand Name: ")
                    warranty = int(input("⚡ Warranty Period (years): "))
                    p = Electronics(pid, name, price, qty, warranty, brand)
                    loading_animation("Adding electronics product")
                    print("\n✅ Electronics product added successfully!")

                elif p_type == "2":
                    expiry = input("📅 Expiry Date (YYYY-MM-DD): ")
                    p = Grocery(pid, name, price, qty, expiry)
                    loading_animation("Adding grocery product")
                    print("\n✅ Grocery product added successfully!")

                elif p_type == "3":
                    size = input("📏 Size (S/M/L/XL): ")
                    material = input("🧵 Material Type: ")
                    p = Clothing(pid, name, price, qty, size, material)
                    loading_animation("Adding clothing product")
                    print("\n✅ Clothing product added successfully!")

                else:
                    print("❌ Invalid product type selected!")
                    sleep(2)
                    continue

                inv.add_product(p)
                print("🎉 Product has been added to inventory!")
                input("\nPress Enter to continue...")

            elif choice == "2":
                clear_screen()
                print("\n💰 === Sell Product === 💰")
                print("━━━━━━━━━━━━━━━━━━━━━")
                pid = input("🔍 Enter Product ID: ")
                qty = int(input("📦 Quantity to sell: "))
                loading_animation("Processing sale")
                inv.sell_product(pid, qty)
                print("✅ Product sold successfully!")
                input("\nPress Enter to continue...")

            elif choice == "3":
                clear_screen()
                print("\n🔍 === Search Products === 🔍")
                print("━━━━━━━━━━━━━━━━━━━━━━━")
                keyword = input("🔍 Enter name/type to search: ")
                loading_animation("Searching")
                results = inv.search_by_name(keyword) + inv.search_by_type(keyword)
                if results:
                    print("\nFound the following products:")
                    for p in results:
                        print(f"\n{p}")
                else:
                    print("\n❌ No products found!")
                input("\nPress Enter to continue...")

            elif choice == "4":
                clear_screen()
                print("\n📋 === Inventory List === 📋")
                print("━━━━━━━━━━━━━━━━━━━━━━━━")
                loading_animation("Loading inventory")
                products = inv.list_all_products()
                if products:
                    for p in products:
                        print(f"\n{p}")
                        print("─" * 40)
                else:
                    print("\n❌ No products in inventory!")
                input("\nPress Enter to continue...")

            elif choice == "5":
                clear_screen()
                print("\n💾 === Save Inventory === 💾")
                print("━━━━━━━━━━━━━━━━━━━━━━━━")
                file = input("📁 Enter filename to save (e.g., data.json): ")
                loading_animation("Saving inventory")
                inv.save_to_file(file)
                print("✅ Inventory saved successfully!")
                input("\nPress Enter to continue...")

            elif choice == "6":
                clear_screen()
                print("\n📂 === Load Inventory === 📂")
                print("━━━━━━━━━━━━━━━━━━━━━━━━")
                file = input("📁 Enter filename to load: ")
                loading_animation("Loading inventory")
                inv.load_from_file(file)
                print("✅ Inventory loaded successfully!")
                input("\nPress Enter to continue...")

            elif choice == "7":
                clear_screen()
                print("\n📊 === Inventory Statistics === 📊")
                print("━━━━━━━━━━━━━━━━━━━━━━━━━━━━")
                loading_animation("Calculating statistics")
                total_products = len(inv.list_all_products())
                print(f"📈 Total Products: {total_products}")
                print(f"💰 Total Value: ${sum(p.price * p.quantity for p in inv.list_all_products()):.2f}")
                input("\nPress Enter to continue...")

            elif choice == "8":
                clear_screen()
                print("\n🔄 === Update Product === 🔄")
                print("━━━━━━━━━━━━━━━━━━━━━━━")
                # Add your update logic here
                print("🚧 Feature coming soon!")
                input("\nPress Enter to continue...")

            elif choice == "9":
                clear_screen()
                print("\n❌ === Delete Product === ❌")
                print("━━━━━━━━━━━━━━━━━━━━━━━")
                # Add your delete logic here
                print("🚧 Feature coming soon!")
                input("\nPress Enter to continue...")

            elif choice == "10":
                clear_screen()
                print("\n👋 Thank you for using Advanced Inventory Management System!")
                loading_animation("Closing system")
                break

            else:
                print("❌ Invalid choice! Please select a number between 1 and 10.")
                sleep(2)

        except ValueError as e:
            print(f"❌ Invalid input: Please enter correct values!")
            sleep(2)
        except Exception as e:
            print(f"❌ Error: {e}")
            sleep(2)

if __name__ == "__main__":
    main()
