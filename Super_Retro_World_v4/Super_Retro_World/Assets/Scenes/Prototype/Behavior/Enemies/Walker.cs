using System.Collections;
using System.Collections.Generic;
using UnityEngine;

// ================================================================================
// Enemy walker class
// Behaviors :
//      - walk from left to right (randomize at Start())
//      - hit player if touched from a side or from below
//      - is killed if touched from upside and provide a boosted jump to the killer
//      - stack for X second if encounter another walker
//      - both walker are killed if they are touched from above at this moment
//      - doing so provide a super super jump
//
// Stack gameplay :
//
//  W1 walks right    W2 walks left
//    [1] --->           <--- [2]
//
//           Both W collide
//              [1][2]
//
//    W1 jump on W2 at collision (stay like this for X seconds)
//               [1]
//               [2]
//
//   Both W split and continu their walk
//          <-- [2][1] -->
public class Walker : Enemy {

    // ================================================================================
    // Define global variables
    // ================================================================================
    // --------------------------------------------------------------------------------
    // walking side
    public bool walkLeft;
    public float walkSpeed;
    // --------------------------------------------------------------------------------
    // physic variables
    public bool hitSmth;
    // --------------------------------------------------------------------------------
    //gameplay variables
    public bool stk; // is the current walker in stack mode
    public Walker otherWalker; // other walker object he is currently stack with
    public bool stkOnTop; // is the current waler on top of the other one
    public float stkDuration; // duration both walker can be staked

    // ================================================================================
    // Use this for initialization
    // ================================================================================
    void Start () {
        // --------------------------------------------------------------------------------
        // Instanciate GO
        go = new GO(gameObject);
        // Instanciate physic variables
        vel = new Vector2(0.0f, 0.0f);
        pos = go.posCen();
        walkSpeed = 2.0f;
        hitSmth = false;
        // instanciate gameplay variables
        stk = false;
        otherWalker = null;
        stkOnTop = false;
        stkDuration = 1.0f;
    }

    // ================================================================================
    // Update is called once per frame
    // ================================================================================
    void Update () {
		
	}
}
