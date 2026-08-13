const sequelize = require('../config/database');
const Customer = require('./Customer');
const Order = require('./Order');
const Product = require('./Product');
const Inventory = require('./Inventory');

// Customer <-> Order
Customer.hasMany(Order, { foreignKey: 'customer_id', as: 'orders' });
Order.belongsTo(Customer, { foreignKey: 'customer_id', as: 'customer' });

// Product <-> Inventory
Product.hasMany(Inventory, { foreignKey: 'product_id', as: 'inventory' });
Inventory.belongsTo(Product, { foreignKey: 'product_id', as: 'product' });

module.exports = { sequelize, Customer, Order, Product, Inventory };
