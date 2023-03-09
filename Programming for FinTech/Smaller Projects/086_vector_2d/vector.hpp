/* write your class interface in this file
   write function definitions only if they are very short
 */
#ifndef Vector2D_H
#define Vector2D_H


class Vector2D
{
   private:
       double x;
      double y;
      
   public:
       
      void initVector(double init_x, double init_y);
      
        double getX() const;
      double getY() const;
      
      double getMagnitude() const;
      /*  magnitude of the vector from the origin
            (0, 0) to (x, y):  sqrt(x^2 + y^2), (Note 
             cmath puts functions in the std   namespace, 
          use the fully qualified name std::sqrt.) */
      
      //double Vector2D operator+(const Vector2D & rhs) const;
      //double operator+(const Vector2D & rhs) const;
      //const Vector2D& operator+(const Vector2D &rhs) const;
      //Vector2D operator+(const Vector2D & rhs) const;
      Vector2D operator+(const Vector2D & rhs);
      /* usual vector addition; returns copy of new vector  */
      
      //double Vector2D operator+(const Vector2D & rhs) const;
      //double operator+(const Vector2D & rhs) const;
      //const Vector2D& operator+=(const Vector2D &rhs);
      //Vector2D operator+=(const Vector2D & rhs) const;
      Vector2D operator+=(const Vector2D & rhs) ;
      /* add the lhs and rhs vector and
            assign the result to the object pointed to by this */
      
      double dot(const Vector2D& rhs) const;
      /* dot product; returns  x1*x2 + y1*y2.  */
      
      void print() const;
       /* print the vector in the format <%.2f, %.2f> */
   
   
};

#endif
