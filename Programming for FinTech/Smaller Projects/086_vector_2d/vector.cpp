#include "vector.hpp"

#include <cmath>
#include <cstdio>



/* write your class implementation in this file
 */

        void Vector2D::initVector(double init_x, double init_y)
        {
            x = init_x;
            y = init_y;         
        }
        
  
        double Vector2D::getMagnitude() const   
        {   
            double magnitude = std::sqrt(x*x + y*y);
            return magnitude;           
        }
    
    
        double Vector2D::Vector2D::getX() const
        {
            return x;
        }
        
        double Vector2D::Vector2D::getY() const
        {
            return y;
        }
        
        
    
         Vector2D Vector2D::operator+(const Vector2D & rhs)
        
        
         {  
            
            // this -> getX() + rhs.getX();
            // x = x + rhs.getX();
            // this -> getY() + rhs.getY();
            // y = y + rhs.getY();
             Vector2D v3; 
             v3.initVector(x, y);
             v3.x = v3.x + rhs.getX();
             v3.y = v3.y + rhs.getY();
             return v3;
         }
        
        
        Vector2D Vector2D::operator+=(const Vector2D & rhs) 
         {
            //x += rhs.getX(); // assignment of member x in read-only object
            //y += rhs.getY(); // assignment of member x in read-only object
            //this -> getX() +=  rhs.getX(); // lvalue required as left operand of assignment
            //this -> getY() +=  rhs.getY(); // lvalue required as left operand of assignment
            //this -> x += rhs.getX(); // assignment of member x in read-only object
            //x = x + rhs.getX();
            //y = y + rhs.getY();
            //return *this;
            // this->m_iNumber += rhs.m_iNumber;
   
            this -> x += rhs.getX();
			this -> y += rhs.getY();
         
             return *this;
            
            
         }

        double Vector2D:: dot(const Vector2D& rhs) const
        {
            double dotProd = x*rhs.x + y*rhs.y;     
            return dotProd;
        }
        
        void Vector2D::print() const
        {
            std::printf("<%.2f, %.2f>", x, y);
        }
    
    



