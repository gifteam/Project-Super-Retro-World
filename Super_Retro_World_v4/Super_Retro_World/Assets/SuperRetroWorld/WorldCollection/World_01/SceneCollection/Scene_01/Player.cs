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
    private int maxXspeed = 6;
    private int maxYspeed = 8;
    private Vector2 XYspeed;
    // -----------------------------------------------------------------------------
    // Jump variables
    public float distToGround;
    private LayerMask groundLayer;
    private int jmpForce = 350;
    public bool isGrounded;
    public bool jmpDmd;
    // -----------------------------------------------------------------------------
    // GO component variables
    private GO go;
    private Rigidbody2D body;
    private BoxCollider2D hitbox;
    private Animator animator;
    private GO trail;

    // =============================================================================
    // Use this for initialization
    // =============================================================================
    void Start()
    {
        Screen.SetResolution(640, 480, true, 60);
        // GO component variables
        this.go = new GO(gameObject);
        this.body = this.go.getRigidbody2D();
        this.hitbox = this.go.getBoxCollider2D();
        this.animator = this.go.getAnimator();
        this.trail = new GO(GameObject.Find("FootTrail"));
        Debug.Log(this.trail);

        // Speed variables
        this.XYspeed = new Vector2(0.0f, 0.0f);

        // Jump variables
        this.groundLayer = LayerMask.GetMask("Ground");
        this.distToGround = this.hitbox.bounds.extents.y + 0.2f;
        this.isGrounded = true;
        this.jmpDmd = false;
    }
    // =============================================================================
    // Update is called once per frame
    // =============================================================================
    void Update()
    {
        //pre round check
        this.isGrounded = this.go.isGrounded(ref this.distToGround, ref this.groundLayer);

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

        if (Input.GetButtonDown("Jump") && this.isGrounded)
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
            this.isGrounded = false;
        }
    }

    // =============================================================================
    // Update animations
    // =============================================================================
    //animation update (only work on "Anim...." variables
    private void updateAnimation()
    {
        //Activate / desactivate running transition
        /*if (this.body.velocity.x != 0.0f)
        {
            this.animator.SetBool("AnimPlayerRunning", true);
        }
        else
        {
            this.animator.SetBool("AnimPlayerRunning", false);
        }*/
        //Activate / desactivate foot trail
        if (this.isGrounded)
        {
            if (!this.trail.getParticleSystem().isPlaying)
            {
                this.trail.getParticleSystem().Play();
                Debug.Log("foot trail play");
            }
        }
        else
        {
            if (this.trail.getParticleSystem().isPlaying)
            {
                this.trail.getParticleSystem().Stop();
                Debug.Log("foot trail stop");
            }
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