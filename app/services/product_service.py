from sqlalchemy import or_
from app.extensions import db
from app.models import Product,Category
class ProductService:
    @staticmethod
    def getAll():
        return Product.query.all()
    def getById(id):
        return Product.query.get(id)
    @staticmethod
    def initData():
        if Product.query.count() == 0:
            category = Category.query.first()
            if not category:
                category = Category.query.first()
                category = Category(name="Default Category")
                db.session.add(category)
                db.session.commit()
            category_id = category.id

            for i in range(1, 11):  
                product = Product(name=f'Product {i}', price=10.99 + i,description = f'Description {i}'
                                  ,category_id = category_id)  
                db.session.add(product)
            db.session.commit()
            print("Inittialized product data with 10 products")
        else:
            print("Product data already initilized")
    @staticmethod
    def create(data):
        """Tạo một sản phẩm mới"""
        product = Product(
            name=data.get('name'),
            price=data.get('price'),
            description=data.get('description'),
            category_id=data.get('category_id')
        )
        db.session.add(product)
        db.session.commit()
        return product

    @staticmethod
    def update(id, data):
        """Cập nhật thông tin sản phẩm"""
        product = Product.query.get(id)
        if not product:
            return None  # Hoặc raise Exception tùy cách xử lý

        # Cập nhật các trường có trong data
        if 'name' in data:
            product.name = data['name']
        if 'price' in data:
            product.price = data['price']
        if 'description' in data:
            product.description = data['description']
        if 'category_id' in data:
            product.category_id = data['category_id']

        db.session.commit()
        return product

    @staticmethod
    def delete(id, soft_delete=True):
        """Xóa sản phẩm (mặc định xóa mềm)"""
        product = Product.query.get(id)
        if not product:
            return False  # Không tìm thấy sản phẩm

        if soft_delete:
            product.is_active = False  # Giả sử có trường này trong model
        else:
            db.session.delete(product)

        db.session.commit()
        return True
    @staticmethod
    def getByCategory(category_id):
        """Lấy danh sách sản phẩm theo danh mục"""
        return Product.query.filter_by(category_id=category_id).all()

    @staticmethod
    def search(keyword):
        """Tìm kiếm sản phẩm theo tên hoặc mô tả"""
        return Product.query.filter(
            or_(
                Product.name.ilike(f"%{keyword}%"),
                Product.description.ilike(f"%{keyword}%")
            )
        ).all()

    @staticmethod
    def filter(price_min=None, price_max=None, category_id=None, sort_by=None):
        """Lọc sản phẩm theo giá, danh mục, và sắp xếp"""
        query = Product.query

        # Lọc theo danh mục
        if category_id:
            query = query.filter(Product.category_id == category_id)

        # Lọc theo khoảng giá
        if price_min is not None:
            query = query.filter(Product.price >= price_min)
        if price_max is not None:
            query = query.filter(Product.price <= price_max)

        # Sắp xếp dữ liệu
        if sort_by:
            if sort_by == "price_asc":
                query = query.order_by(Product.price.asc())
            elif sort_by == "price_desc":
                query = query.order_by(Product.price.desc())
            elif sort_by == "name_asc":
                query = query.order_by(Product.name.asc())
            elif sort_by == "name_desc":
                query = query.order_by(Product.name.desc())

        return query.all()
    @staticmethod
    def paginate(page, per_page):
        """Phân trang danh sách sản phẩm"""
        return Product.query.paginate(page=page, per_page=per_page, error_out=False)

    @staticmethod
    def count():
        """Đếm số lượng sản phẩm"""
        return Product.query.count()

    @staticmethod
    def exists(id):
        """Kiểm tra xem sản phẩm có tồn tại không"""
        return db.session.query(Product.query.filter_by(id=id).exists()).scalar()

    @staticmethod
    def bulkInsert(products):
        """Thêm nhiều sản phẩm cùng lúc"""
        product_objects = [Product(**data) for data in products]
        db.session.bulk_save_objects(product_objects)
        db.session.commit()
        return product_objects

    @staticmethod
    def bulkUpdate(product_updates):
        """Cập nhật nhiều sản phẩm cùng lúc"""
        for update in product_updates:
            product = Product.query.get(update.get("id"))
            if product:
                if "name" in update:
                    product.name = update["name"]
                if "price" in update:
                    product.price = update["price"]
                if "description" in update:
                    product.description = update["description"]
                if "category_id" in update:
                    product.category_id = update["category_id"]
        db.session.commit()
        return True

    @staticmethod
    def bulkDelete(ids, soft_delete=True):
        """Xóa nhiều sản phẩm cùng lúc (mặc định xóa mềm)"""
        products = Product.query.filter(Product.id.in_(ids)).all()
        if not products:
            return False

        if soft_delete:
            for product in products:
                product.is_active = False  # Giả sử có cột này
        else:
            for product in products:
                db.session.delete(product)

        db.session.commit()
        return True