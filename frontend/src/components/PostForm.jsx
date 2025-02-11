import React, { useState } from "react";

const PostForm = () => {
  const [postContent, setPostContent] = useState("");
  const [selectedPlatforms, setSelectedPlatforms] = useState({
    facebook: false,
    twitter: false,
    linkedin: false,
  });
  const [scheduleTime, setScheduleTime] = useState("");
  const [status, setStatus] = useState("");

  const handlePlatformChange = (platform) => {
    setSelectedPlatforms((prev) => ({
      ...prev,
      [platform]: !prev[platform],
    }));
  };

  const handleSubmit = (e) => {
    e.preventDefault();

    if (!postContent) {
      alert("Please write a post before submitting.");
      return;
    }

    const selected = Object.values(selectedPlatforms).some(Boolean);
    if (!selected) {
      alert("Please select at least one platform.");
      return;
    }

    setStatus("Posting...");

    const postData = {
      content: postContent,
      platforms: selectedPlatforms,
      scheduleTime: scheduleTime || "Now",
    };

    // Simulate API call
    setTimeout(() => {
      console.log("Post Data:", postData);
      setStatus("Post successfully submitted!");
      setPostContent("");
      setSelectedPlatforms({
        facebook: false,
        twitter: false,
        linkedin: false,
      });
      setScheduleTime("");
    }, 2000);
  };

  return (
    <div className="bg-white shadow-md rounded-lg p-6 w-full max-w-md">
      <h1 className="text-2xl font-bold mb-4 text-center">Create Post</h1>

      <textarea
        className="w-full p-3 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 mb-4"
        rows="5"
        placeholder="Write your post here..."
        value={postContent}
        onChange={(e) => setPostContent(e.target.value)}
      ></textarea>

      <div className="mb-4">
        <label className="block font-semibold mb-2">Select Platforms:</label>
        <div className="flex justify-between">
          {["facebook", "twitter", "linkedin"].map((platform) => (
            <label key={platform} className="flex items-center space-x-2">
              <input
                type="checkbox"
                checked={selectedPlatforms[platform]}
                onChange={() => handlePlatformChange(platform)}
              />
              <span className="capitalize">{platform}</span>
            </label>
          ))}
        </div>
      </div>

      <div className="mb-4">
        <label className="block font-semibold mb-2">
          Schedule Time (optional):
        </label>
        <input
          type="datetime-local"
          className="w-full p-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
          value={scheduleTime}
          onChange={(e) => setScheduleTime(e.target.value)}
        />
      </div>

      <button
        className="w-full bg-blue-600 text-white py-2 rounded-md hover:bg-blue-700 transition"
        onClick={handleSubmit}
      >
        Post Now
      </button>

      {status && <p className="text-green-600 mt-4 text-center">{status}</p>}
    </div>
  );
};

export default PostForm;
