/*
 * kalman.cpp
 *
 *  Created on: Sep 2, 2015
 *      Author: rfal
 */

#include "kalman.h"


kalman::kalman()
{
	// TODO Auto-generated constructor stub

}

kalman::kalman(const matrix<double>& a, const matrix<double>& b, const matrix<double>& c,const matrix<double>& q, const matrix<double>& p, const matrix<double>& r, const vector<double>& mu)
{

	A = new matrix<double>(a);
	B = new matrix<double>(b);
	C = new matrix<double>(c);
	Q = new matrix<double>(q);
	P = new matrix<double>(p);
	R = new matrix<double>(r);
	state = new vector<double>(mu);


}
bool kalman::update( vector<double>& u , vector<double>&  z)
{
	vector<double> predictionState,updateState,tempCState;//the state
	matrix<double> transpose,tempPC,tempCP,tempCPR,inverse,k,tempKP;
	identity_matrix<double> eye ((int)state->size());
	bool update = false;

	//Prediction step
	predictionState = prod(*A, *state) + prod(*B,u);

	transpose =  prod(*A,*P);

 	*P= prod(transpose,trans(*A)) + *Q;

 	//update step
 	tempPC = prod(*P, trans(*C));

 	tempCP = prod(*C, *P);

 	tempCPR = prod(tempPC,trans(*C)) + *R;
 	//find if it can be inversed
 	inverse = tempCPR*0.0;
 	update = rfal_inverse(tempCPR, inverse);

 	if(update)
 	{
 		std::cout<<"update "<<update<<std::endl;
 		k = prod(tempPC,inverse);
 		tempCState = prod(*C,predictionState);
 		updateState = predictionState +  prod(k, z - tempCState);
 		tempKP = prod(k,*C);
 		*P = prod( eye - tempKP,*P );

 		*state = updateState;
 	}
	//std::cout<<eye<<std::endl;


  return update;


}

vector<double>* kalman::getState()
{

	return state;

}

template<class T>
bool kalman::rfal_inverse( const matrix<T>& input , matrix<T>& inverse )
{
	// create a working copy of the input
	  matrix<T> A( input );

	  // create a permutation matrix for the LU-factorization
	  permutation_matrix<std::size_t> pm( A.size1( ) );

	  // perform LU-factorization

	  int res = lu_factorize( A , pm );

	  if( res != 0  )
	    return false;

	  // create identity matrix of "inverse"
	  inverse.assign( identity_matrix<T>( A.size1( ) ) );
	  std::cout<<"foo"<<std::endl;
	  // backsubstitute to get the inverse
	  lu_substitute( A , pm , inverse );

	  return true;
}

kalman::~kalman()
{
	// TODO Auto-generated destructor stub
}

