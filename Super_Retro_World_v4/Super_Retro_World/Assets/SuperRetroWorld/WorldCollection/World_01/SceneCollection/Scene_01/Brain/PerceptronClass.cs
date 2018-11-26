using System.Collections;
using System.Collections.Generic;
using UnityEngine;

public class Perceptron
{
    //public float m_weigth;
    public float m_value;
    public List<PerceptronInput> m_inputList;
    public List<PerceptronOutput> m_outputList;
    //public BlocPop m_blocPop;
    public Control m_control;
    public List<double> m_dnaPart;
    public GO m_geko;
    public GO m_tracker;

    public Perceptron (Control a_control, GO a_geko, GO a_tracker)
    {
        m_dnaPart = new List<double>();
        m_control = a_control;
        m_geko = a_geko;
        m_tracker = a_tracker;
        m_inputList = new List<PerceptronInput>();
        m_outputList = new List<PerceptronOutput>();

        m_inputList.Add(new PerceptronInput(m_geko, "X"));
        m_inputList.Add(new PerceptronInput(m_geko, "Y"));
        m_inputList.Add(new PerceptronInput(m_tracker, "X"));
        m_inputList.Add(new PerceptronInput(m_tracker, "Y"));

        int l_outputs = m_control.m_keys.Count;
        for (int i_outputIndex = 0; i_outputIndex < l_outputs; i_outputIndex++)
        {
            m_outputList.Add(new PerceptronOutput(m_control, i_outputIndex));
        }
    }

    public void setWeigth(Perceptron a_parentPerceptron)
    {
        for (int i_inputIndex = 0; i_inputIndex < m_inputList.Count; i_inputIndex ++)
        {
            m_inputList[i_inputIndex].m_weigth = a_parentPerceptron.m_inputList[i_inputIndex].m_weigth;
        }
        for (int i_outputIndex = 0; i_outputIndex < m_outputList.Count; i_outputIndex++)
        {
            m_outputList[i_outputIndex].m_weigth = a_parentPerceptron.m_outputList[i_outputIndex].m_weigth;
        }

        bool l_mutateInputWeigth = false;
        bool l_mutateOutputWeigth = false;
        float l_random = Random.Range(0f, 100f);
        if (l_random < 5f)
        {
            l_mutateInputWeigth = true;
        }
        else if (l_random < 10f)
        {
            l_mutateOutputWeigth = true;
        }

        if (l_mutateInputWeigth)
        {
            int l_index = (int) Random.Range(0f, m_inputList.Count - 1);
            m_inputList[l_index].m_weigth = Random.Range(-1.0f, 1.0f);
        }
        else if (l_mutateOutputWeigth)
        {
            int l_index = (int) Random.Range(0f, m_outputList.Count - 1);
            m_outputList[l_index].m_weigth = Random.Range(-1.0f, 1.0f);
        }
    }

    public void getDnaPart()
    {
        m_dnaPart.Clear();
        foreach (PerceptronInput i in m_inputList)
        {
            m_dnaPart.Add(i.m_weigth);
        }
        foreach (PerceptronOutput o in m_outputList)
        {
            m_dnaPart.Add(o.m_weigth);
        }
    }

    public void update()
    {
        m_value = 0;
        foreach (PerceptronInput i in m_inputList)
        {
            i.update();
            m_value += i.m_value;
        }
        //m_value += m_weigth;

        if (m_value > 1f)
        {
            m_value = 1f;
        }
        else if (m_value < -1f)
        {
            m_value = -1f;
        }

        foreach (PerceptronOutput o in m_outputList)
        {
            o.update(m_value);
        }
    }

    public void showInputWeight()
    {
        string l_listValues = "";
        foreach (PerceptronInput i in m_inputList)
        {
            l_listValues += i.m_weigth + ";";
        }
        Debug.Log(l_listValues);
    }
}

public class PerceptronInput
{
    //public int m_blocIndex;
    public GO m_spy;
    public string m_spyComponent;
    public float m_weigth;
    public float m_value;
    //public BlocPop m_blocPop;

    public PerceptronInput(GO a_spy, string a_spyComponent)
    {
        m_spy = a_spy;
        m_spyComponent = a_spyComponent;
        m_weigth = Random.Range(-1.0f, 1.0f);
        m_value = 0;
    }

    public void update()
    {
        if (m_spyComponent.Equals("X"))
        {
            m_value = m_spy.posCen().x * m_weigth;
        }
        else if (m_spyComponent.Equals("Y"))
        {
            m_value = m_spy.posCen().y * m_weigth;
        }
    }
}

public class PerceptronOutput
{
    public int m_keyIndex;
    public float m_weigth;
    public float m_value;
    public Control m_control;

    public PerceptronOutput(Control a_control, int a_keyIndex)
    {
        m_control = a_control;
        m_keyIndex = a_keyIndex; // Mathf.RoundToInt(Random.Range(0.0f, m_control.m_keys.Count - 1f));
        m_weigth = Random.Range(-1.0f, 1.0f);
    }

    public void update(float a_value)
    {
        m_value = a_value * m_weigth;
        m_control.m_keys[m_keyIndex] += m_value;
    }
}
