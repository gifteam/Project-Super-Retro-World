using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class player_code : MonoBehaviour {

    public int playerMaxHSpeed = 10;
    public bool playerDirRight = true;
    public int playerJumpForce = 1000;
    public float playerHSpeed = 0;
    public Vector2 playerVel;

    // Use this for initialization
    void Start ()
    {
        playerVel = new Vector2(0.0f, 0.0f);
    }
	
	// Update is called once per frame
	void Update ()
    {
        //main movement update
        PlayerMove();
	}

    // Movement of the player object
    void PlayerMove()
    {
        //get controls
        playerHSpeed = Input.GetAxis("Horizontal");
        //update animation

        //update player jump
        if (Input.GetButtonDown("Jump"))
        {
            Jump();
        }

        //update player direction
        if ((playerHSpeed < 0.0f && !playerDirRight) || (playerHSpeed > 0.0f && playerDirRight))
        {
            Flip();
        }
        //update player physics
        playerVel.x = playerHSpeed * playerMaxHSpeed;
        playerVel.y = gameObject.GetComponent<Rigidbody2D>().velocity.y;
        gameObject.GetComponent<Rigidbody2D>().velocity = playerVel;
    }

    // Jump method
    void Jump()
    {
        gameObject.GetComponent<Rigidbody2D>().AddForce(Vector2.up * playerJumpForce);
    }


    // Flip player direction
    void Flip()
    {
        playerDirRight = !playerDirRight;
    }
}

