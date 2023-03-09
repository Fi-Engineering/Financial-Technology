#ifndef __EXPR_H___
#define __EXPR_H___
#include <cstdio>
#include <cstdlib>
#include <string>
#include <sstream>


class Expression
{
  public: Expression() {}
  virtual std::string toString() const = 0;
  virtual ~Expression() {}
};

class NumExpression : public Expression
{
  long num;

  public: NumExpression(long i) : num(i) {}
  virtual std::string toString() const {
    std::stringstream answer;
    answer << num;
    return answer.str();
  }
  virtual ~NumExpression() {}
};

class PlusExpression : public Expression
{
  Expression * left;
  Expression * right;

  public: PlusExpression(Expression * lhs, Expression * rhs) : left(lhs), right(rhs) {}
  virtual std::string toString() const {
    std::stringstream answer;
    answer << "(" << left->toString() << " + " << right->toString() << ")";
    return answer.str();
  }
  virtual ~PlusExpression() {
    delete left;
    delete right;
  }
};

#endif
