float fare(int p, int s, int d){
	float Y = p + 5*0.01*s + (5/12)*0.01*d;
	return Y;
}
int main(){
	float Y = fare()
	printf("The fare is %f", Y);
}
