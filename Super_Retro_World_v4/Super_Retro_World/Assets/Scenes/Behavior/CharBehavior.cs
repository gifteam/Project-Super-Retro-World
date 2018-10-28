using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class CharBehavior : MonoBehaviour {

    // define physic behavior
    public const int maxXspeed = 10;
    public const int maxYspeed = 10;
    public Vector2 XYspeed;

    public float distToGround;
    public LayerMask groundLayer;
    public const int jmpForce = 350;
    public bool jmpAvail;
    public bool jmpDmd;

    public bool dirRight = true;
    public bool dirLeft = false;

    public Rigidbody2D body;
    public BoxCollider2D hitbox;

    // Use this for initialization
    void Start ()
    {
        hitbox = gameObject.GetComponent<BoxCollider2D>();
        body = gameObject.GetComponent<Rigidbody2D>();

        XYspeed = new Vector2(0.0f, 0.0f);

        groundLayer = LayerMask.GetMask("Ground");
        distToGround = hitbox.bounds.extents.y + 0.1f;
        jmpAvail = true;
        jmpDmd = false;
    }
	
	// Update is called once per frame
	void Update ()
    {
        //pre round check
        jmpAvail = isGrounded();

        // get control
        getKeyboard();

        // movement update
        applyForce();
	}

    bool isGrounded()
    {
        Vector2 direction = Vector2.down;

        RaycastHit2D hit = Physics2D.Raycast(getPos(), direction, distToGround, groundLayer);
        if (hit.collider != null)
        {
            return true;
        }

        return false;
    }

    void getKeyboard()
    {
        XYspeed.x = Input.GetAxis("Horizontal") * maxXspeed;
        XYspeed.y = getCurrentVelY();

        if (Input.GetButtonDown("Jump") && jmpAvail)
        {
            jmpDmd = true;
        }
    }

    float getCurrentVelX ()
    {
        return body.velocity.x;
    }

    float getCurrentVelY ()
    {
        return body.velocity.y;
    }

    Vector2 getPos()
    {
        return transform.position;
    }

    void applyForce ()
    {
        // X force
        body.velocity = XYspeed;

        // Y force
        if (jmpDmd)
        {
            body.AddForce(Vector2.up * jmpForce);
            jmpDmd = false;
            jmpAvail = false;
        }
    }
}

