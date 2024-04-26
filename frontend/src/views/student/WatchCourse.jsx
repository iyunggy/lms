import React, { useState, useEffect } from "react";
import { Link } from "react-router-dom";
import moment from "moment";
import parse from "html-react-parser";

import BaseHeader from "../partials/BaseHeader";
import BaseFooter from "../partials/BaseFooter";
import Sidebar from "./Partials/Sidebar";
import Header from "./Partials/Header";
import useAxios from "../../utils/useAxios";
import UserData from "../plugin/UserData";
import { useNavigate } from "react-router-dom";
import ReactPlayer from "react-player";

function WatchCourse() {
  const [courses, setCourses] = useState([]);
  const [stats, setStats] = useState([]);
  const [fetching, setFetching] = useState(true);
  const nav = useNavigate();

  const fetchData = () => {
    setFetching(true);

    useAxios()
      .get(`student/course-list/${UserData()?.user_id}/`)
      .then((res) => {
        console.log(res.data);
        setCourses(res.data);
        setFetching(false);
      });
  };

  useEffect(() => {
    fetchData();
  }, []);

  const handleSearch = (event) => {
    const query = event.target.value.toLowerCase();
    console.log(query);
    if (query === "") {
      fetchData();
    } else {
      const filtered = courses.filter((c) => {
        return c.course.title.toLowerCase().includes(query);
      });
      setCourses(filtered);
    }
  };
  return (
    <>
      <BaseHeader />

      <section className="pt-5 pb-5">
        <div className="container">
          {/* Header Here */}
          <Header />
          <div className="row mt-0 mt-md-4">
            {/* Sidebar Here */}
            <Sidebar />
            <div className="col-lg-9 col-md-8 col-12">
              <h4 className="mb-0 mb-4">{courses[0]?.course.title}</h4>

              {fetching === true && <p className="mt-3 p-3">Loading...</p>}

              {fetching === false && (
                <div className="card mb-4">
                  <div className="w-full">
                    {" "}
                    <ReactPlayer
                      controls={true}
                      url={courses[0]?.course.video_url}
                      width="100%"
                    />
                  </div>
                  <div className="card-header mt-2">
                    <h5>Level : {parse(courses[0]?.course.level)}</h5>
                    <h5>Bahasa : {parse(courses[0]?.course.language)}</h5>
                  </div>
                  <div className="card-body">
                    {parse(courses[0]?.course.description)}
                  </div>
                </div>
              )}
            </div>
          </div>
        </div>
      </section>

      <BaseFooter />
    </>
  );
}

export default WatchCourse;
