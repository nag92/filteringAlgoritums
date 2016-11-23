//============================================================================
// Name        : filteringProccess.cpp
// Author      : Nathaniel Goldfarb
// Version     :
// Copyright   : Your copyright notice
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
//#include "kalman.h"
#include "OutlierFilter.h"
#include <boost/numeric/ublas/matrix.hpp>
#include <boost/numeric/ublas/lu.hpp>
#include <boost/numeric/ublas/io.hpp>

//using namespace std;
using namespace boost::numeric::ublas;

int main()
{

	matrix<double> a( 2 , 2 );
	  a( 0 , 0 ) = 4.0;
	  a( 0 , 1 ) = 3.0;
	  a( 1 , 0 ) = 3.0;
	  a( 1 , 1 ) = 2.0;

	matrix<double> b,c,r,q,p;
	b = a;
	c = a;
	r = a;
	q = a;
	p = a;
    vector<double> mu(2);
	mu(0) =1;
	mu(1) = 1;

	//std::cout<<a<<std::endl;
	std::cout<<mu<<std::endl;
	//std::cout<<trans(a)<<std::endl;
	kalman test(a,b,c,r,q,p,mu);
	std::cout<<"hello"<<std::endl;
	test.update(mu,mu);
	std::cout<<*test.getState()<<std::endl;

	/*

	int window = 10;
	  int size  = 2;
	  int weight[2];
	  int range[2];
	  int* w;
	  int* r;
	  double condin = 2.77;

	  range[0] = 0;
	  range[1] = 1;
	  r = range;

	  OutlierFilter temp(size,condin,window,r);
	  BLAS::vector<double> points(3);
	  temp.isGood(points);

	  //points(2) = 2;





	 std::cout<<"....................."<<std::endl;
	 points(0) = 3;
	 points(1) = 6;
	 temp.isGood(points);
	 std::cout<<"....................."<<std::endl;
	 points(0) = 3;
	 points(1) = 6;
	 temp.isGood(points);
	 std::cout<<"....................."<<std::endl;
	 points(0) = 3;
	 points(1) = 6;
	 temp.isGood(points);
	 std::cout<<"....................."<<std::endl;
	 points(0) = 3;
	 points(1) = 6;
	 temp.isGood(points);
*/
	return 0;
}
