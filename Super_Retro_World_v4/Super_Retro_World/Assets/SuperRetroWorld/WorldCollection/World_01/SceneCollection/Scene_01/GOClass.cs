using System.Collections;
using System.Collections.Generic;
using UnityEngine;

// ================================================================================
// GameObject geometry and trigonometry class
// ================================================================================

public class GO {

    // =============================================================================
    // Class variable
    // =============================================================================
    private GameObject go; // GameObject variable

    // =============================================================================
    // Constructor
    // =============================================================================
    public GO(GameObject go_)
    {
        go = go_;
    }
    // =============================================================================
    // Return many specifics GO positions from the "transform" component
    //
    //                                           Cen Top
    //     ,-------------,         Top Left [+]----[+]----[+] Top Right
    //     |             |                   |             |
    //     |             |                   |     Cen     |
    //     | GameObject  |   ==>   Cen Left [+]   -[+]-   [+] Cen Right
    //     |   (Rect)    |                   |      '      |
    //     |             |                   |             |
    //     '-------------'         Bot Left [+]----[+]----[+] Bot Right          
    //                                           Cen Bot
    //
    //    Y
    //    ^
    //    |
    //    +---> X
    // =============================================================================
    // -----------------------------------------------------------------------------
    // Center position 
    public Vector2 posCen()
    {
        return go.transform.position;
    }
    // -----------------------------------------------------------------------------
    // Center left position
    public Vector2 posCenLeft()
    {
        Vector2 offset = new Vector2(-0.5f, 0.0f);
        return this.posCenX(ref offset);
    }
    // -----------------------------------------------------------------------------
    // Center Right position
    public Vector2 posCenRight()
    {
        Vector2 offset = new Vector2(0.5f, 0.0f);
        return this.posCenX(ref offset);
    }
    // -----------------------------------------------------------------------------
    // Center Top position
    public Vector2 posCenTop()
    {
        Vector2 offset = new Vector2(0.0f, 0.5f);
        return this.posCenX(ref offset);
    }
    // -----------------------------------------------------------------------------
    // Center Bottom position
    public Vector2 posCenBot()
    {
        Vector2 offset = new Vector2(0.0f, -0.5f);
        return this.posCenX(ref offset);
    }
    // -----------------------------------------------------------------------------
    // Top Left position
    public Vector2 posTopLeft()
    {
        Vector2 offset = new Vector2(-0.5f, 0.5f);
        return this.posCenX(ref offset);
    }
    // -----------------------------------------------------------------------------
    // Top Right position
    public Vector2 posTopRight()
    {
        Vector2 offset = new Vector2(0.5f, 0.5f);
        return this.posCenX(ref offset);
    }
    // -----------------------------------------------------------------------------
    // Bot Left position
    public Vector2 posBotLeft()
    {
        Vector2 offset = new Vector2(-0.5f, -0.5f);
        return this.posCenX(ref offset);
    }
    // -----------------------------------------------------------------------------
    // Bot Right position
    public Vector2 posBotRight()
    {
        Vector2 offset = new Vector2(0.5f, -0.5f);
        return this.posCenX(ref offset);
    }
    // -----------------------------------------------------------------------------
    // Return a position with offset times the GO scale (see public "posCen..." functions for examples calls)
    private Vector2 posCenX(ref Vector2 offset)
    {
        // Step 1 : get position / scale of the GO
        Vector2 pos = this.posCen();
        Vector3 scl = this.scale();
        // Step 2 : get box Collider offset and size (%)
        Vector2 boxOffset = new Vector2(0.0f, 0.0f);
        Vector2 boxSize = new Vector2(1.0f, 1.0f);
        if (this.hastBoxCollider2D())
        {
            boxOffset = this.getBoxCollider2D().offset;
            boxSize = this.getBoxCollider2D().size;
        }
        // Step 3 : edit current pos and scl according to hitbox parameters
        pos.x += boxOffset.x * scl.x;
        pos.y += boxOffset.y * scl.y;
        scl.x *= boxSize.x;
        scl.y *= boxSize.y;

        this.offsetPos(ref pos, ref offset, ref scl);
        return pos;
    }
    // -----------------------------------------------------------------------------
    // Offset the given position by an offset of the GO scale
    private void offsetPos(ref Vector2 pos, ref Vector2 offset, ref Vector3 scl)
    {
        pos.x += offset.x * scl.x;
        pos.y += offset.y * scl.y;
    }
    // -----------------------------------------------------------------------------
    // Return the scale of the GO
    private Vector3 scale()
    {
        return this.go.transform.localScale;
    }

    // =============================================================================
    // Return true if the current GO is touching its "groundlayer"
    // Perfomr 3 raycast to make sure the ground is below feet
    //
    //                                
    //     ,-------------,                   ,-------------,
    //     |             |                   '             '
    //     |             |                   '   Raycast   '
    //     | GameObject  |   ==>    Raycast [+]    [+]    [+] Raycast     
    //     |   (Rect)    |                   |      |      |
    //     |             |                   |      |      | 
    //     '-------------'                   V------V------V 
    //   ################### Ground        ################### Ground
    //
    //    Y
    //    ^
    //    |
    //    +---> X
    // =============================================================================
    public bool isGrounded(ref float distToGround, ref LayerMask groundLayer)
    {
        Vector2 direction = Vector2.down;

        RaycastHit2D hitLeft = Physics2D.Raycast(this.posCenLeft(), direction, distToGround, groundLayer);
        RaycastHit2D hitCen = Physics2D.Raycast(this.posCen(), direction, distToGround, groundLayer);
        RaycastHit2D hitRight = Physics2D.Raycast(this.posCenRight(), direction, distToGround, groundLayer);

        if (hitLeft.collider != null || hitRight.collider != null || hitCen.collider != null)
        {
            return true;
        }

        return false;
    }

    // =============================================================================
    // Position update
    // =============================================================================
    public void setPos(Vector2 pos)
    {
        this.go.transform.position = pos;
    }

    // =============================================================================
    // Return many GO component
    // =============================================================================
    // -----------------------------------------------------------------------------
    // Return TRUE if the GO has a BoxCollider2D, FALSE overwise
    public bool hastBoxCollider2D()
    {
        return this.go.GetComponent<BoxCollider2D>();
    }
    // -----------------------------------------------------------------------------
    // Return BoxCollider2D component of the GO
    public BoxCollider2D getBoxCollider2D()
    {
        return this.go.GetComponent<BoxCollider2D>();
    }
    // -----------------------------------------------------------------------------
    // Return Rigidbody2D component of the GO
    public Rigidbody2D getRigidbody2D()
    {
        return this.go.GetComponent<Rigidbody2D>();
    }
    // -----------------------------------------------------------------------------
    // Return Rigidbody2D component of the GO
    public Animator getAnimator()
    {
        return this.go.GetComponent<Animator>();
    }
}



