#include <bits/stdc++.h>
using namespace std;

using ll = long long;

struct Seg {
  ll l,r,d;
};

ll conv(ll x, vector<Seg>& a) {
  int lo=0, hi=(int)a.size()-1;
  while (lo<=hi) {
    int mid = (lo+hi) >> 1;
    if (x < a[mid].l) {
      hi=mid-1;
    }
    else if(x>= a[mid].r) {
      lo=mid+1;
    }
    else {
      return x + a[mid].d;
    }
  }
  return x;

}

int main() {
  ios::sync_with_stdio(false);
  cin.tie(nullptr);

  string filename;
  cin >> filename;
  ifstream f(filename);

  string line;
  getline(f, line);

  vector<pair<ll,ll>> seeds;
  stringstream ss(line.substr(line.find(':')+1));
  ll s,len;
  while (ss>>s>>len) seeds.push_back({s,len});

  vector<vector<Seg>> maps;
  while (getline(f, line)) {
    if(line.empty()) continue;

    if(line.find("map:")!=string::npos) {
      vector<Seg> cur;
      while (getline(f,line) && !line.empty()) {
        stringstream ss(line);
        ll dst,src,len;
        ss >> dst >> src >> len;
        cur.push_back({src,src+len,dst-src});
      }
      sort(cur.begin(),cur.end(),[](const Seg& a, const Seg& b) {
        return a.l < b.l;
      });
      maps.push_back(cur);
    }
  }

  ll ans=(ll)4e18;
  for(auto [start, len] : seeds) {
    for(ll x=start; x < start + len; x++) {
      ll y = x;
      for(auto& mp : maps) {
        y=conv(y,mp);
      }
      ans=min(ans,y);
    }
  }
  cout << ans << "\n";
}