using System.Collections;
using System.Collections.Generic;
using UnityEngine;

// ================================================================================
// Main scene camera behavior
// ================================================================================

public class CamBehavior : MonoBehaviour {

    // =============================================================================
    // Define class variables
    // =============================================================================

    // -----------------------------------------------------------------------------
    // Self GO (GameObject) to interact with
    private GO go;
    // -----------------------------------------------------------------------------
    // Space boundaries for the camera center 
    private int xMin;
    private int xMax;
    private int yMin;
    private int yMax;
    // -----------------------------------------------------------------------------
    // Target the camera follow (can only follow one target)
    private GO target;

    // =============================================================================
    // Initialisation
    // =============================================================================
    void Start () {

        //set self gameobject instance
        go = new GO(gameObject);

        // look for one specific target to center the camera with
        target = new GO(GameObject.FindGameObjectWithTag("Player"));

        // set the camera center boundaries
        xMin = -10;
        xMax = 100;
        yMin = 3;
        yMax = 10;
}
    // =============================================================================
    // Update is called once per frame
    // =============================================================================
    void LateUpdate() {

        updatePos();
    }
    // -----------------------------------------------------------------------------
    // Update the position to mathc the target (within the camera bounds)
    private void updatePos()
    { 
        Vector2 targetPos = target.posCen();

        float camX = Mathf.Clamp(targetPos.x, xMin, xMax);
        float camY = Mathf.Clamp(targetPos.y, yMin, yMax);
        float camZ = gameObject.transform.position.z;

        go.setPos(new Vector3(camX, camY, camZ));
    }
}
