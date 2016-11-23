/*
 * kalman.h
 *
 *  Created on: Sep 2, 2015
 *      Author: rfal, Nathaniel Goldfarb
 */

#ifndef KALMAN_H_
#define KALMAN_H_
#include  <boost/numeric/ublas/matrix.hpp>
#include <boost/numeric/ublas/lu.hpp>
#include <boost/numeric/ublas/io.hpp>
#include <boost/numeric/ublas/vector.hpp>
#include <boost/numeric/ublas/vector_proxy.hpp>
#include <boost/numeric/ublas/vector_sparse.hpp>
#include <boost/numeric/ublas/triangular.hpp>


using namespace boost::numeric::ublas;
class kalman
{
public:
	kalman();
	virtual ~kalman();
	kalman(const matrix<double>&,//A
			const matrix<double>&,//B
			const matrix<double>&,//C
			const matrix<double>&,//Q
			const matrix<double>&,//P
			const matrix<double>&,//R
			const vector<double>&);//mu


	matrix<double>* A; //state matrix
	matrix<double>* B; //Control matrix
	matrix<double>* C; //measurement model
	matrix<double>* Q; //Process noise covariance
	matrix<double>* P; //predeciton
	matrix<double>* R; // measurement noise covariance
	vector<double>* state; // state

	//update the state

	bool update( vector<double>&, vector<double>& );
	vector<double>* getState();

private:
	template<class T>
	bool rfal_inverse( const matrix<T>&  , matrix<T>&  ) ;

};

#endif /* KALMAN_H_ */
