import java.io.*;
import java.util.*;
import java.lang.*;

public class UnionFind {

  private int[] parents;
  private int[] sizes;

  static String YES = "yes\n";
  static String NO = "no\n";

  public UnionFind(int N){
    this.parents = new int[N];
    this.sizes = new int[N];
    for (int i=0; i<N;i++){
      this.parents[i] = i;
      this.sizes[i] = 1;
    }
  }

  public boolean isConnected(int x, int y){
    if (x == y){
      return true;
    }
    return find(x) == find(y);
  }

  public void union(int x, int y){
    int x_root = find(x);
    int y_root = find(y);

    if (x_root == y_root){
      return;
    }

    if (sizes[x_root] < sizes[y_root]){
      adaptSizes(x_root,y_root);
    } else {
      adaptSizes(y_root,x_root);
    }
    return;
  }

  public void adaptSizes(int slave, int master){
    this.parents[slave] = master;
    this.sizes[master] += sizes[slave];
  }

  public int find(int a){
    int root = a;
    while (root != this.parents[a]){
      root = this.parents[a];
    }
    return root;
  }

  public int findParent(int a){
    int root = a;
    while (root != parents[a]){
      // Traversing upp the hierarchy
      root = parents[a];
    }
    int a_temp = a;
    while (a_temp != root) {
      int a_prime = parents[a_temp];
      parents[a] = root;
      a_temp = a_prime;
    }
    return root;
  }

  public static void main(String[] args) throws IOException {
    BufferedReader in = new BufferedReader(new InputStreamReader(System.in),1024*1024);
    PrintWriter out = new PrintWriter(new BufferedOutputStream(System.out));

    String line = in.readLine();

    int pos = line.lastIndexOf(' ');
    int N = Integer.parseInt(line.substring(0,pos));
    int Q = Integer.parseInt(line.substring(pos+1,line.length()));

    UnionFind uf = new UnionFind(N);

    for(int i=0;i<Q;i++){
      String query = in.readLine();

      pos = query.lastIndexOf(' ');
      char op = line.charAt(0);

      int a = Integer.parseInt(query.substring(2,pos));
      int b = Integer.parseInt(query.substring(pos+1,query.length()));
      if (op == '=') {
        uf.union(a,b);
      } else {
        out.print(uf.isConnected(a,b) ? YES : NO);
      }
    }

    out.flush();
    out.close();
  }

}
