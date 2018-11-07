using System.Collections;
using System.Collections.Generic;
using UnityEngine;

// =============================================================================
// Moving filter class
// =============================================================================
public class FilterClass : MonoBehaviour {

    // =============================================================================
    // Class variable
    // =============================================================================
    // GO component variables
    private GO go;
    // Geometric public variables
    public Vector2 posInit;
    public float speed;
    public float dist;
    // Geometric private variable
    public float angle;

    // =============================================================================
    // Use this for initialization
    // =============================================================================
    void Start () {
        // set GO instance
        this.go = new GO(gameObject);

        // set geometric variables
        this.posInit = this.go.posCen();
        this.speed = 1.0f;
        this.dist  = 1.0f;
        this.angle = 0.0f;
    }

    // =============================================================================
    // Update is called once per frame
    // =============================================================================
    void Update () {
        // increment angle value depending on speed factor
        this.angle += 0.01f * this.speed;

        // update current Y position with sin(angle)
        Vector2 pos = this.go.posCen();
        pos.y = posInit.y + ( Mathf.Sin(this.angle) * this.dist );

        //update Go position with the new pos
        this.go.setPos(pos);
    }
}
