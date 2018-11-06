using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Player : MonoBehaviour
{

    // =============================================================================
    // Class variable
    // =============================================================================

    // -----------------------------------------------------------------------------
    // Speed variables
    private int maxXspeed = 8;
    private int maxYspeed = 8;
    private Vector2 XYspeed;
    // -----------------------------------------------------------------------------
    // Jump variables
    public float distToGround;
    private LayerMask groundLayer;
    private int jmpForce = 350;
    public bool jmpAvail;
    public bool jmpDmd;
    // -----------------------------------------------------------------------------
    // GO component variables
    private GO go;
    private Rigidbody2D body;
    private BoxCollider2D hitbox;
    private Animator animator;

    // =============================================================================
    // Use this for initialization
    // =============================================================================
    void Start()
    {
        // GO component variables
        this.go = new GO(gameObject);
        this.body = this.go.getRigidbody2D();
        this.hitbox = this.go.getBoxCollider2D();
        this.animator = this.go.getAnimator();

        // Speed variables
        this.XYspeed = new Vector2(0.0f, 0.0f);

        // Jump variables
        this.groundLayer = LayerMask.GetMask("Ground");
        this.distToGround = this.hitbox.bounds.extents.y + 0.2f;
        this.jmpAvail = true;
        this.jmpDmd = false;
    }
    // =============================================================================
    // Update is called once per frame
    // =============================================================================
    void Update()
    {
        //pre round check
        this.jmpAvail = this.go.isGrounded(ref this.distToGround, ref this.groundLayer);

        // get control
        this.getKeyboard();

        // movement update
        this.applyForce();

        //animation update
        this.updateOrientation();
        this.updateAnimation();
    }
    // -----------------------------------------------------------------------------
    // Get the keyboard inputs
    private void getKeyboard()
    {
        this.XYspeed.x = Input.GetAxis("Horizontal") * this.maxXspeed;
        this.XYspeed.y = this.getCurrentVel().y;

        if (Input.GetButtonDown("Jump") && this.jmpAvail)
        {
            this.jmpDmd = true;
        }
    }
    // -----------------------------------------------------------------------------
    // Get velocity
    private Vector2 getCurrentVel()
    {
        return this.body.velocity;
    }
    // -----------------------------------------------------------------------------
    // Get the keyboard inputs
    private void applyForce()
    {
        // X force
        this.body.velocity = this.XYspeed;

        // Y force
        if (this.jmpDmd)
        {
            this.body.AddForce(Vector2.up * this.jmpForce);
            this.jmpDmd = false;
            this.jmpAvail = false;
        }
    }

    // =============================================================================
    // Update animations
    // =============================================================================
    //animation update (only work on "Anim...." variables
    private void updateAnimation()
    {
        //Activate / desactivate running transition
        if (this.body.velocity.x != 0.0f)
        {
            this.animator.SetBool("AnimPlayerRunning", true);
        }
        else
        {
            this.animator.SetBool("AnimPlayerRunning", false);
        }
    }
    // -----------------------------------------------------------------------------
    //animation update (only work on "Anim...." variables
    private void updateOrientation()
    {
        //Update sprite orientation (flipX)
        if (this.body.velocity.x < 0.0f)
        {
            gameObject.GetComponent<SpriteRenderer>().flipX = true;
        }
        else
        {
            gameObject.GetComponent<SpriteRenderer>().flipX = false;
        }
    }

    // =============================================================================
    // Events
    // =============================================================================
    // -----------------------------------------------------------------------------
    // coin collection
    void OnTriggerEnter2D(Collider2D other)
    {
        if (other.gameObject.CompareTag("Coin"))
        {
            other.gameObject.SetActive(false);
        }
    }
}