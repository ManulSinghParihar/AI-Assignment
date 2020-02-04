/*

							!!! 8 Queens Problem !!!

States: 1 <= state <= 8
		At any given point of time, the board would contain atleast
		1 queen and atmost 8 queens.

Initial State: Initially, a sinle queen is placed on the board,
		starting from the top-left corner of the board.

Function: The queens must be placed on the board such that it is not
		under attack by the rest of the queens presently on the board.

Goal State: All the 8 queens are successfully placed on the board
		such that no queen is under attack by any of the rest 7 queens
		on the board at any pint of time.

Path cost: 1 per level. At depth 1, the cost is 1,
		at depth 2, the cost is 2 and so on. The depth of the tree 
		would atmost be 8 since there are 8 queens. Therefore the 
		total path cost for the solution would be 8.

*/


#include <bits/stdc++.h>
#define pq priority_queue < board, vector < board >, compare > q
#define pb push_back
#define V vector < int >
#define bOp bool operator()(board b1, board b2)
using namespace std;

int ANS = 0;

struct board{
	V states;
	int cost;
	int next_board;
};

struct compare{
	bOp{
		return b1.cost < b2.cost;
	}
};

bool isFinal(V vec);
board mB(board x, int next_row);
bool isSafe(V present, int r, int c);
void print(V v);
void ucs(pq, int n);

int main(){
	int x;
	cout<<"Enter the size of the board :\t";
	cin>>x;

	pq;
	board f;
	f.states.pb(0);    			// Putting Queen at (0, 0)
	f.cost = 0;      		  	// g(0) = 0 as the g(x) function in the UCS Algorithm, here cost
	f.next_board = 1;          	// next_board is the position for the next Queen
	q.push(f);

	ucs(q,x);

	cout << "Total Possible Answers are\t" << ANS <<endl;
}

board mB(board x, int next_row){
	V vec;
	if(x.states.size()) vec.assign(x.states.begin(), x.states.end());
	vec.pb(next_row);
	board b;
	b.cost = x.cost;
	b.next_board = vec.size();
	b.states = vec;
	return b;
}

bool isSafe(V present, int r, int c){
	for(int i=0; i<present.size(); i++) if(present[i] == r || abs(present[i]-r) == abs(c-i)) return false;
	return true;
}

bool isFinal(V vec){
	for(int i=0; i<vec.size(); i++){
		for(int j=0; j<vec.size(); j++){
			if(i==j) continue;
			if(vec[i] == vec[j] || abs(vec[i]-vec[j]) == abs(i-j)) return false;
		}
	}
	return true;
}

void print(V v){
	for(auto i : v) cout << i << " ";
	cout << "\n";
}

void ucs(pq, int n){
	int BOARD = 1;          			// BOARD stores value in case queue becomes empty 
									  	// Index of the row to start next UCS
	while(true){
		board b;
		if(q.size()){
			b = q.top();
			q.pop();
		}
		else{
			if(BOARD == n) return;
			b.states.pb(BOARD++);
			b.cost = 0;              	// value is next board in case queue is empty
			b.next_board = 1;
		}
		if(b.states.size() == n){
			if(isFinal(b.states)){
				ANS++;
				print(b.states);
			}
			continue;
		}
		for(int i=0; i<n; i++){
			if(isSafe(b.states, i, b.next_board)){
				board x = mB(b, i);
				q.push(x);
			}
		}
	}
}
