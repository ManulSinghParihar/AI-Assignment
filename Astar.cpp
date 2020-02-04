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
	int func;
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
void astar(pq, int n);

int main(){
	int x;
	cout<<"Enter the size of the board :\t";
	cin>>x;

	pq;
	board f;
	f.states.pb(0);    			// Putting Queen at (0, 0)
	f.cost = 0;      		  	// g(0) = 0 as the g(x) function in the Astar Algorithm, here cost
	f.next_board = 1;          	// next_board is the position for the next Queen
	f.func = x - 0;				// h(i) = n - i (Heuristic function)
	q.push(f);

	astar(q,x);

	cout << "Total Possible Answers are\t" << ANS <<endl;
}

board mB(board x, int y, int next_row){
	V vec;
	if(x.states.size()) vec.assign(x.states.begin(), x.states.end());
	vec.pb(next_row);
	board b;
	b.cost = x.cost + x.func + 1;
	b.next_board = vec.size();
	x.func = y - x.states.size();
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

void astar(pq, int n){
	int BOARD = 1;          			// BOARD stores value in case queue becomes empty 
									  	// Index of the row to start next Astar
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
			b.func = n - 0;
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
				board x = mB(b, n, i);
				q.push(x);
			}
		}
	}
}
