package com.careerlens.controller;

import com.careerlens.client.AiServiceClient;
import lombok.RequiredArgsConstructor;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Map;

@RestController
@RequestMapping("/api/interview")
@CrossOrigin(origins = "*")
@RequiredArgsConstructor
public class InterviewController {

    private final AiServiceClient aiServiceClient;

    @PostMapping("/start")
    public ResponseEntity<Map<String, Object>> startInterview(@RequestBody Map<String, Object> request) {
        String resumeText = (String) request.getOrDefault("resume_text", "");
        String jobDescription = (String) request.getOrDefault("job_description", "");
        List<String> topics = (List<String>) request.get("topics");

        Map<String, Object> question = aiServiceClient.startInterview(resumeText, jobDescription, topics);
        return ResponseEntity.ok(question);
    }

    @PostMapping("/respond")
    public ResponseEntity<Map<String, Object>> submitAnswer(@RequestBody Map<String, Object> request) {
        String question = (String) request.getOrDefault("question", "");
        String answer = (String) request.getOrDefault("answer", "");
        String resumeContext = (String) request.getOrDefault("resume_context", "");
        String jobContext = (String) request.getOrDefault("job_context", "");

        Map<String, Object> result = aiServiceClient.submitInterviewAnswer(question, answer, resumeContext, jobContext);
        return ResponseEntity.ok(result);
    }
}
