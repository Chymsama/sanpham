#!/usr/bin/env python
# coding: utf-8

# In[1]:


ProductList =[]

def getinfpro(ProductList,ProductId):
    for product in ProductList:
        if product["ID"] == ProductId:
            return product
    return None

def getall(ProductList):
    print("Danh sách sản phẩm :")
    for product in ProductList:
        print(f"ID: {product['ID']}- Name: {product['name']}")

def addpro(ProductList):
    ProductId = int(input('Nhập ID sản phầm: '))
    ProductName= input('Nhập tên sản phẩm: ')
    Productnew = {"ID" : ProductId,"name": ProductName }
    ProductList.append(Productnew)
    print('Đã thêm sản phẩm thành công:')

def editname(ProductList):
    ProductId = int(input('Nhập ID sản phẩm cần sửa tên:'))
    product = getinfpro(ProductList,ProductId)
    if product:
        NewName = input('Nhập và tên thay đổi: ')
        product['name'] = NewName
        print('Cập nhật tên thành công')
    else:
        print('Không tìm thấy ID sản phẩm.')

def deletepro(ProductList):
    ProductId= int(input('Nhập ID sản phẩm cần xóa: '))
    product= getinfpro(ProductList,ProductId)
    if product:
        ProductList.remove(product)
        print('Xóa sản phẩm thành công')
    else:
        print('Không tìm thấy ID sản phẩm.')

def main():
    while True:
        print("\nCHƯƠNG TRÌNH QUẢN LÝ SẢN PHẨM")
        print("1. Hiển thị danh sách sản phẩm")
        print("2. Thêm sản phẩm mới")
        print("3. Sửa tên sản phẩm")
        print("4. Xoá sản phẩm")
        print("0. Thoát chương trình")
        choice = input("Nhập lựa chọn của bạn: ")

        if choice == "1":
            getall(ProductList)
        elif choice == "2":
            addpro(ProductList)
        elif choice == "3":
            editname(ProductList)
        elif choice == "4":
            deletepro(ProductList)
        elif choice == "0":
            print('Bye Bye')
            break
        else:
            print("Lựa chọn không hợp lệ. Vui lòng chọn lại.")
            
main()

