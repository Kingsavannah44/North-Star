const { DataTypes } = require('sequelize');
const sequelize = require('../config/database');

const Order = sequelize.define('Order', {
  id: {
    type: DataTypes.INTEGER,
    primaryKey: true,
    autoIncrement: true,
  },
  order_number: {
    type: DataTypes.STRING(20),
    allowNull: false,
    unique: true,
  },
  customer_id: {
    type: DataTypes.INTEGER,
    allowNull: false,
  },
  status: {
    type: DataTypes.ENUM('Processing', 'Shipped', 'Delivered', 'Cancelled'),
    allowNull: false,
    defaultValue: 'Processing',
  },
  tracking_number: {
    type: DataTypes.STRING(50),
    allowNull: true,
  },
  estimated_delivery: {
    type: DataTypes.DATEONLY,
    allowNull: true,
  },
}, {
  tableName: 'orders',
  timestamps: true,
  createdAt: 'created_at',
  updatedAt: 'updated_at',
});

module.exports = Order;
