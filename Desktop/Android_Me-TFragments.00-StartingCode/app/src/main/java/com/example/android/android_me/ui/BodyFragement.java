package com.example.android.android_me.ui;

import android.app.Fragment;
import android.os.Bundle;
import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;

import com.example.android.android_me.R;
import com.example.android.android_me.data.AndroidImageAssets;

/**
 * Created by jaswanth on 18/05/17.
 */

public class BodyFragement extends Fragment {
    //mandatary for creating the fragment
    public BodyFragement() {

    }

    @Override
    public View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstance){
        //inflate the android me fragment layout
        View rootView = inflater.inflate(R.layout.fragement_body_layout,container,false);
        // get the reference to imageView  in the fragment layout
        ImageView imageView = (ImageView) rootView.findViewById(R.id.body_part_image_view);
        //set the image view to daisplay
        imageView.setImageResource(AndroidImageAssets.getHeads().get(0));

        return rootView;
    }
}
